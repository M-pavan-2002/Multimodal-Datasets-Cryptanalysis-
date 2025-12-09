async function sendData() {
  const text = document.getElementById('textInput').value;
  const imageInput = document.getElementById('imageInput').files[0];

  if (!text || !imageInput) {
    alert('Please provide both encrypted text and an image!');
    return;
  }

  const canvas = document.getElementById('imagePreview');
  const ctx = canvas.getContext('2d');
  const img = new Image();

  img.onload = async () => {
    ctx.drawImage(img, 0, 0, 64, 64);
    const imageData = ctx.getImageData(0, 0, 64, 64);
    const grayscale = [];

    const data = imageData.data;
    for (let i = 0; i < data.length; i += 4) {
      const gray = Math.round((data[i] + data[i+1] + data[i+2]) / 3);
      grayscale.push(gray);
    }

    const res = await fetch('http://127.0.0.1:5000/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        text: text.split('').map(c => c.charCodeAt(0)),
        image: grayscale
      })
    });

    const result = await res.json();
    document.getElementById('result').innerHTML = `
      <strong>🔍 Result:</strong> ${result.verdict}<br>
      <strong>📊 Score:</strong> ${result.score.toFixed(3)}
    `;
  };

  img.src = URL.createObjectURL(imageInput);
}
