const userName = document.getElementById("name");
const courseName = document.getElementById("courseName");
const result = document.getElementById("result");
const submitBtn = document.getElementById("getCirtificate");
const cirtificateid = document.getElementById("cirtificateid");

const { PDFDocument, rgb, degrees } = PDFLib;


const capitalize = (str, lower = false) =>
  (lower ? str.toLowerCase() : str).replace(/(?:^|\s|["'([{])+\S/g, (match) =>
    match.toUpperCase()
  );

submitBtn.addEventListener("click", () => {
  const val = capitalize(userName.innerText);
    generatePDF(val);
  
});

const generatePDF = async (name) => {
  const existingPdfBytes = await fetch("../../studentProfile/cartificate.pdf").then((res) =>
    res.arrayBuffer()
  );

  // Load a PDFDocument from the existing PDF bytes
  const pdfDoc = await PDFDocument.load(existingPdfBytes);
  pdfDoc.registerFontkit(fontkit);

  //get font
  const fontBytes = await fetch("../../studentProfile/Sanchez-Regular.ttf").then((res) =>
    res.arrayBuffer()
  );

  // Embed our custom font in the document
  const SanChezFont = await pdfDoc.embedFont(fontBytes);

  // Get the first page of the document
  const pages = pdfDoc.getPages();
  const firstPage = pages[0];

  // Draw a string of text diagonally across the first page
  firstPage.drawText(name, {
    x: 230,
    y: 290,
    size: 50,
    font: SanChezFont,
    color: rgb(0,0,0),
  });
  // date
  let currentDate = new Date();
  let cDay = currentDate.getDate();
  let cMonth = currentDate.getMonth() + 1;
  let cYear = currentDate.getFullYear();

  firstPage.drawText(cDay + "/" + cMonth + "/" + cYear, {
    x: 220,
    y: 145,
    size: 13,
    font: SanChezFont,
    color: rgb(0, 0, 0),
  });

  // Course grade 
  firstPage.drawText(`'`+result.value+`'`, {
    x: 305,
    y: 188,
    size: 22,
    font: SanChezFont,
    color: rgb(0, 0, 0),
  });
  // Course name 
  firstPage.drawText(`'`+courseName.innerText+`'`, {
    x: 378,
    y: 188,
    size: 24,
    font: SanChezFont,
    color: rgb(0, 0, 0),
  });
  // Course name 
  firstPage.drawText(`SI NO:`+cirtificateid.innerText, {
    x: 100,
    y: 100,
    size: 12,
    font: SanChezFont,
    color: rgb(0, 0, 0),
  });



  // Serialize the PDFDocument to bytes (a Uint8Array)
  const pdfBytes = await pdfDoc.save();
  console.log("Done creating");

  // this was for creating uri and showing in iframe

  // const pdfDataUri = await pdfDoc.saveAsBase64({ dataUri: true });
  // document.getElementById("pdf").src = pdfDataUri;

  var file = new File(
    [pdfBytes],
    "Certificate.pdf",
    {
      type: "application/pdf;charset=utf-8",
    }
  );
  saveAs(file);
};

// init();
