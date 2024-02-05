const fs = require("fs");
const { createCanvas, loadImage } = require("canvas");

const userList = fs.readFileSync("list.bxe", "utf-8").split("\n");

loadImage("bg.png").then((bgImage) => {
  userList.forEach((user, index) => {
    if (user.startsWith("@" || user.startsWith("\n"))) {
      return;
    }

    const canvas = createCanvas(bgImage.width, bgImage.height);
    const ctx = canvas.getContext("2d");

    const [name, age, city] = user.split(",");

    ctx.drawImage(bgImage, 0, 0);

    ctx.font = "bold 12px Arial";
    ctx.fillStyle = "black";
    ctx.textAlign = "center";

    // PRO TIP
    // Upload the bg.png to https://pixspy.com/ to get pixel coordinates
    // PRO TIP

    ctx.fillText(name, 179, 117);
    ctx.fillText(age, 97, 212);
    ctx.fillText(city, 261, 210);

    const certificateName = `output/${name.trim()}.png`;
    const out = fs.createWriteStream(certificateName);
    const stream = canvas.createPNGStream();
    stream.pipe(out);
  });
});
