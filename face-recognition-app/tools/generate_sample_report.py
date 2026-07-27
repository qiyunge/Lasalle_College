from __future__ import annotations

import html
import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "Face_Recognition_Final_Report_Sample.docx"


def esc(text: object) -> str:
    return html.escape(str(text), quote=False)


def run(text: str, *, bold: bool = False, italic: bool = False, size: int = 21) -> str:
    props = []
    if bold:
        props.append("<w:b/>")
    if italic:
        props.append("<w:i/>")
    props.append(f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>')
    return (
        "<w:r><w:rPr>" + "".join(props) + "</w:rPr>"
        f'<w:t xml:space="preserve">{esc(text)}</w:t></w:r>'
    )


def paragraph(
    text: str = "",
    *,
    style: str | None = None,
    align: str | None = None,
    bold: bool = False,
    italic: bool = False,
    size: int = 21,
    before: int = 0,
    after: int = 80,
    line: int = 250,
    keep: bool = False,
) -> str:
    pprops = []
    if style:
        pprops.append(f'<w:pStyle w:val="{style}"/>')
    if align:
        pprops.append(f'<w:jc w:val="{align}"/>')
    pprops.append(f'<w:spacing w:before="{before}" w:after="{after}" w:line="{line}" w:lineRule="auto"/>')
    if keep:
        pprops.append("<w:keepNext/>")
    return f"<w:p><w:pPr>{''.join(pprops)}</w:pPr>{run(text, bold=bold, italic=italic, size=size)}</w:p>"


def heading(text: str, level: int = 1) -> str:
    sizes = {1: 30, 2: 25, 3: 22}
    return paragraph(
        text,
        style=f"Heading{level}",
        bold=True,
        size=sizes[level],
        before=130 if level > 1 else 0,
        after=70,
        line=240,
        keep=True,
    )


def bullet(text: str) -> str:
    return (
        '<w:p><w:pPr><w:pStyle w:val="ListBullet"/>'
        '<w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>'
        '<w:spacing w:after="35" w:line="235" w:lineRule="auto"/>'
        '<w:ind w:left="420" w:hanging="240"/></w:pPr>'
        + run(text, size=20)
        + "</w:p>"
    )


def table(headers: list[str], rows: list[list[object]], widths: list[int] | None = None) -> str:
    widths = widths or [int(9000 / len(headers))] * len(headers)
    grid = "".join(f'<w:gridCol w:w="{w}"/>' for w in widths)
    xml_rows = []
    for row_index, row in enumerate([headers, *rows]):
        cells = []
        for value, width in zip(row, widths):
            shade = '<w:shd w:fill="D9EAF7"/>' if row_index == 0 else ""
            cell_text = paragraph(str(value), bold=row_index == 0, size=19, after=30, line=220)
            cells.append(
                f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{shade}</w:tcPr>{cell_text}</w:tc>'
            )
        xml_rows.append("<w:tr>" + "".join(cells) + "</w:tr>")
    borders = (
        '<w:tblBorders><w:top w:val="single" w:sz="4" w:color="808080"/>'
        '<w:left w:val="single" w:sz="4" w:color="808080"/>'
        '<w:bottom w:val="single" w:sz="4" w:color="808080"/>'
        '<w:right w:val="single" w:sz="4" w:color="808080"/>'
        '<w:insideH w:val="single" w:sz="4" w:color="B0B0B0"/>'
        '<w:insideV w:val="single" w:sz="4" w:color="B0B0B0"/></w:tblBorders>'
    )
    return f'<w:tbl><w:tblPr><w:tblW w:w="9000" w:type="dxa"/>{borders}</w:tblPr><w:tblGrid>{grid}</w:tblGrid>{"".join(xml_rows)}</w:tbl>'


def page_break() -> str:
    return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'


def build_document() -> str:
    evaluation = json.loads((ROOT / "models" / "evaluation_report.json").read_text(encoding="utf-8"))
    history = json.loads((ROOT / "models" / "training_history.json").read_text(encoding="utf-8"))
    best = history["search"]["best_parameters"]
    body: list[str] = []

    # Page 1: cover and executive summary
    body += [
        paragraph("FACE DETECTION & RECOGNITION APP", align="center", bold=True, size=38, before=600, after=180),
        paragraph("Final Project Report", align="center", bold=True, size=28, after=300),
        paragraph("Student: Qiyun Ge", align="center", size=22, after=60),
        paragraph("Student ID: [INSERT STUDENT ID]", align="center", size=22, after=60),
        paragraph("Course: [INSERT COURSE NAME AND CODE]", align="center", size=22, after=60),
        paragraph("Instructor: [INSERT INSTRUCTOR NAME]", align="center", size=22, after=60),
        paragraph("Submission Date: [INSERT DATE]", align="center", size=22, after=260),
        heading("Executive Summary", 1),
        paragraph(
            "This project implements an end-to-end real-time face recognition application. It collects a balanced two-class dataset, detects and crops faces, standardizes images, trains an artificial neural network (ANN), and exposes recognition through both OpenCV and a FastAPI web interface. The final dataset contains 200 raw images: 100 images of the author and 100 consented images grouped as other people. A multilayer perceptron (MLP) classifier was selected through randomized five-fold cross-validation. The best cross-validation accuracy was 97.14%, while the independent 30-image test set achieved 100% accuracy. These results demonstrate that the pipeline works under the sampled conditions, but they do not establish broad real-world generalization.",
            size=20,
            after=110,
            line=235,
        ),
        paragraph("Keywords: face detection, face recognition, ANN, MLP, OpenCV, FastAPI", italic=True, size=19),
    ]

    # Page 2: collection and preprocessing
    body += [page_break(), heading("1. Dataset Collection and Preparation"),
        heading("1.1 Collection procedure", 2),
        paragraph(
            "The raw dataset was created specifically for this project using camera-based image capture. It contains 200 images divided equally between the target identity, “qiyun ge,” and an “others” class. This exceeds the assignment minimum of 40 images and preserves the required 50% share for the student's own face. Images were captured with variations in frontal and non-frontal pose, facial expression, viewing angle, distance, and lighting. All other participants must have provided consent before their photographs were collected; written confirmation should be retained separately if required by the instructor.", size=20),
        table(["Class", "Raw images", "Share", "Purpose"], [["qiyun ge", 100, "50%", "Known target identity"], ["others", 100, "50%", "Non-target examples"]], [2000, 1500, 1200, 4300]),
        heading("1.2 Face preprocessing", 2),
        paragraph(
            "Each image is read with OpenCV and passed through the same preprocessing function used during inference. The pipeline detects a face, crops the detected region with a configurable margin, resizes it to a fixed input size, optionally converts it to grayscale, and scales pixel values from 0–255 to 0–1. Class names are derived from folder names, which keeps labels reproducible and avoids a separate annotation file.", size=20),
        heading("1.3 Augmentation and split", 2),
        paragraph(
            "Mild augmentation improves robustness without substantially changing identity. The implementation supports horizontal flipping with probability 0.5, rotation within ±10 degrees, and brightness scaling from 0.85 to 1.15. A deterministic seed of 42 is used for repeatability. The data are split by class using a 70/15/15 ratio, corresponding to 140 training, 30 validation, and 30 test images when all 200 images are used.", size=20),
        table(["Stage", "Ratio", "Images", "Use"], [["Training", "70%", 140, "Fit ANN and cross-validation"], ["Validation", "15%", 30, "Model checking"], ["Test", "15%", 30, "Final independent evaluation"]], [1900, 1200, 1400, 4500]),
    ]

    # Page 3: architecture and training
    body += [page_break(), heading("2. Recognition Model and Training"),
        heading("2.1 Detection and feature pipeline", 2),
        paragraph(
            "The application supports three face detectors: OpenCV Haar Cascade, OpenCV YuNet, and an optional YOLOv8 face detector. YuNet is the default because it offers a practical balance between CPU speed and robustness. For every detection, the bounding box is clipped to the frame, the face is cropped, and the crop is converted to the same normalized representation used during training. The flattened pixel vector is then passed to the classifier.", size=20),
        heading("2.2 ANN architecture", 2),
        paragraph(
            "The recognizer is a scikit-learn Pipeline containing StandardScaler followed by MLPClassifier. Standardization reduces scale imbalance between input features. The selected neural network has one hidden layer with 64 neurons and ReLU activation. The output layer represents the two learned classes and predict_proba supplies the confidence score. L2 regularization (alpha) reduces overfitting, and the initial learning rate controls gradient-update size.", size=20),
        table(["Component", "Selected setting"], [["Input", "Flattened normalized face pixels"], ["Feature scaling", "StandardScaler"], ["Hidden layers", str(best["classifier__hidden_layer_sizes"])], ["Activation", best["classifier__activation"]], ["L2 alpha", best["classifier__alpha"]], ["Initial learning rate", best["classifier__learning_rate_init"]], ["Output", "Two-class probabilities"]], [3200, 5800]),
        heading("2.3 Model selection", 2),
        paragraph(
            f"RandomizedSearchCV evaluated {history['search']['candidates']} parameter combinations using stratified five-fold cross-validation. Candidate choices included 64, 128, and 128–64 hidden-unit configurations; ReLU and tanh activations; three regularization values; and two learning rates. Accuracy was the selection metric, random_state was fixed at 42, and the best pipeline was refitted on the full training set. Training converged in {history['iterations']} iterations, with loss decreasing from {history['loss'][0]:.4f} to {history['loss'][-1]:.4f}.", size=20),
    ]

    # Page 4: evaluation
    body += [page_break(), heading("3. Evaluation Results"),
        heading("3.1 Quantitative results", 2),
        paragraph(
            f"The selected model achieved {history['search']['best_score'] * 100:.2f}% mean accuracy during five-fold cross-validation. On the held-out test set, it correctly classified all {evaluation['test_samples']} samples, producing {evaluation['accuracy'] * 100:.1f}% accuracy. Precision, recall, and F1-score were 1.00 for both classes. The confusion matrix contains no off-diagonal errors.", size=20),
        table(["Metric", "others", "qiyun ge", "Overall"], [["Precision", "1.00", "1.00", "—"], ["Recall", "1.00", "1.00", "—"], ["F1-score", "1.00", "1.00", "1.00"], ["Support", "15", "15", "30"], ["Accuracy", "—", "—", "100%"]], [2200, 1900, 2200, 1800]),
        heading("3.2 Confusion matrix", 2),
        table(["Actual / Predicted", "others", "qiyun ge"], [["others", 15, 0], ["qiyun ge", 0, 15]], [3900, 2500, 2600]),
        heading("3.3 Interpretation", 2),
        paragraph(
            "The perfect test score indicates that the two classes are separable within this dataset and that the training and inference preprocessing steps are consistent. The slightly lower cross-validation score is a more cautious estimate because it aggregates performance across multiple training/validation partitions. The result should not be interpreted as universal 100% recognition: the test set is small, the images come from a limited acquisition process, and samples from the same capture sessions may share background, camera, and lighting characteristics.", size=20),
        paragraph(
            "A stronger evaluation would collect a new session on a different day and device, add more unrelated people, test backlighting and partial occlusion, and report false-accept and false-reject rates across several confidence thresholds.", size=20),
    ]

    # Page 5: application
    body += [page_break(), heading("4. Real-Time Application"),
        heading("4.1 Runtime workflow", 2),
        paragraph(
            "The final application combines webcam capture, face detection, preprocessing, ANN inference, and visualization. In the browser version, JavaScript captures a compressed JPEG frame approximately three times per second and sends it to the same-origin FastAPI endpoint. The server detects every face, classifies each crop, and returns a label, confidence, and bounding box. The interface overlays the returned results on the camera view.", size=20),
        table(["Step", "Operation", "Output"], [["1", "Capture webcam frame", "JPEG image"], ["2", "Detect faces with YuNet", "Bounding boxes"], ["3", "Crop and preprocess", "Normalized vectors"], ["4", "MLP probability prediction", "Label + confidence"], ["5", "Apply unknown threshold", "Known name or Unknown"], ["6", "Render overlay", "Box, label, confidence"]], [900, 4800, 3300]),
        heading("4.2 Unknown-person handling", 2),
        paragraph(
            "The network always returns class probabilities for its learned labels. To meet the assignment requirement, the predictor compares the maximum probability with a configurable threshold. If confidence is below the threshold, the displayed label becomes “Unknown”; otherwise, the predicted class is shown. This threshold provides practical rejection behavior, although a two-class closed-set classifier is not a complete open-set recognition solution.", size=20),
        heading("4.3 Interface and API", 2),
        bullet("The camera page displays bounding boxes, predicted names, and confidence scores."),
        bullet("GET /api/v1/health reports readiness and model-loading errors."),
        bullet("GET /api/v1/model reports the detector, threshold, and known classes."),
        bullet("POST /api/v1/recognize accepts a JPEG and returns structured face results."),
        bullet("GET /api/docs provides interactive OpenAPI documentation."),
        paragraph("[INSERT SCREENSHOT: browser camera page showing bounding boxes, labels, and confidence scores.]", italic=True, align="center", size=19, before=80),
    ]

    # Page 6: limitations and conclusion
    body += [page_break(), heading("5. Limitations, Improvements, and Conclusion"),
        heading("5.1 Limitations", 2),
        bullet("The test set contains only 30 images and may not represent unseen environments."),
        bullet("Only one named identity is modeled; all other people share a broad “others” class."),
        bullet("Similar capture backgrounds can allow the classifier to learn incidental visual cues."),
        bullet("A raw-pixel MLP is sensitive to alignment, illumination, pose, blur, and occlusion."),
        bullet("Confidence from a closed-set classifier is not perfectly calibrated for unknown people."),
        heading("5.2 Proposed improvements", 2),
        paragraph(
            "Future work should collect more participants across independent sessions and devices, maintain identity-separated train/test collection, and evaluate difficult conditions such as masks, glasses, side profiles, and low light. Face alignment based on eye landmarks would reduce pose variation. A pretrained face-embedding model could replace raw pixels, after which similarity distance and a calibrated threshold could support stronger open-set recognition. Threshold selection should use validation ROC or precision–recall analysis rather than a manually chosen value. Privacy can be improved through explicit consent records, retention limits, encrypted storage, and deletion procedures.", size=20),
        heading("5.3 Conclusion", 2),
        paragraph(
            "The project satisfies the required AI pipeline from data collection to a working real-time application. It uses a balanced 200-image dataset, reproducible preprocessing and augmentation, an ANN selected through cross-validation, independent evaluation, and a simple web interface. The measured results are strong for the project dataset: 97.14% cross-validation accuracy and 100% test accuracy. The main lesson is that successful face recognition depends not only on the classifier, but also on consistent face detection, careful dataset design, realistic evaluation, and responsible handling of biometric data.", size=20),
        heading("References", 2),
        paragraph("[1] OpenCV Documentation, Face Detection and Image Processing APIs.\n[2] Scikit-learn Documentation, MLPClassifier, Pipeline, StandardScaler, and RandomizedSearchCV.\n[3] FastAPI Documentation, Request Handling and OpenAPI Integration.\n[4] Project source code and generated training/evaluation artifacts.", size=18, line=220),
        paragraph("Submission note: replace all bracketed placeholders and insert one application screenshot before exporting the final PDF.", italic=True, size=18, before=90),
    ]

    section = (
        '<w:sectPr><w:pgSz w:w="12240" w:h="15840"/>'
        '<w:pgMar w:top="720" w:right="850" w:bottom="720" w:left="850" w:header="360" w:footer="360"/>'
        '<w:footerReference w:type="default" r:id="rId2"/>'
        '<w:cols w:space="720"/><w:docGrid w:linePitch="360"/></w:sectPr>'
    )
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        '<w:body>' + "".join(body) + section + '</w:body></w:document>'
    )


def build_docx() -> None:
    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
 <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
 <Default Extension="xml" ContentType="application/xml"/>
 <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
 <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
 <Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
 <Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>
 <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
 <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>'''
    root_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
 <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
 <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>'''
    document_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
 <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>
 <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>
</Relationships>'''
    styles = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
 <w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Aptos" w:hAnsi="Aptos"/><w:sz w:val="21"/><w:lang w:val="en-CA"/></w:rPr></w:rPrDefault></w:docDefaults>
 <w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/></w:style>
 <w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:rPr><w:b/><w:color w:val="1F4E79"/><w:sz w:val="30"/></w:rPr></w:style>
 <w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:rPr><w:b/><w:color w:val="2F75B5"/><w:sz w:val="25"/></w:rPr></w:style>
 <w:style w:type="paragraph" w:styleId="ListBullet"><w:name w:val="List Bullet"/><w:basedOn w:val="Normal"/><w:qFormat/></w:style>
</w:styles>'''
    numbering = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
 <w:abstractNum w:abstractNumId="0"><w:multiLevelType w:val="singleLevel"/><w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="•"/><w:lvlJc w:val="left"/><w:pPr><w:tabs><w:tab w:val="num" w:pos="420"/></w:tabs><w:ind w:left="420" w:hanging="240"/></w:pPr><w:rPr><w:rFonts w:ascii="Symbol" w:hAnsi="Symbol"/></w:rPr></w:lvl></w:abstractNum>
 <w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num>
</w:numbering>'''
    footer = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:t>Face Detection &amp; Recognition App  |  Page </w:t></w:r><w:r><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:instrText> PAGE </w:instrText></w:r><w:r><w:fldChar w:fldCharType="end"/></w:r></w:p></w:ftr>'''
    core = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>Face Detection &amp; Recognition App - Final Project Report</dc:title><dc:creator>Qiyun Ge</dc:creator><dc:subject>Final Project Report Sample</dc:subject><dcterms:created xsi:type="dcterms:W3CDTF">2026-07-21T00:00:00Z</dcterms:created></cp:coreProperties>'''
    app = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"><Application>Microsoft Office Word</Application><Pages>6</Pages><Company>LaSalle College</Company></Properties>'''

    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", content_types)
        archive.writestr("_rels/.rels", root_rels)
        archive.writestr("word/document.xml", build_document())
        archive.writestr("word/_rels/document.xml.rels", document_rels)
        archive.writestr("word/styles.xml", styles)
        archive.writestr("word/numbering.xml", numbering)
        archive.writestr("word/footer1.xml", footer)
        archive.writestr("docProps/core.xml", core)
        archive.writestr("docProps/app.xml", app)
    print(OUTPUT)


if __name__ == "__main__":
    build_docx()
