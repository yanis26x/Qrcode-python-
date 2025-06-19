package yanis26x;

import com.google.zxing.BarcodeFormat;
import com.google.zxing.Writer;
import com.google.zxing.client.j2se.MatrixToImageConfig;
import com.google.zxing.client.j2se.MatrixToImageWriter;
import com.google.zxing.common.BitMatrix;
import com.google.zxing.qrcode.QRCodeWriter;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.util.Objects;

public class RUN_THIS {

    public static boolean createQRcode(QRcode qrcode, String logoPath) {
        BitMatrix bitMatrix;
        Writer writer = new QRCodeWriter();

        try {
            bitMatrix = writer.encode(qrcode.getMessage(), BarcodeFormat.QR_CODE, qrcode.getWidth(), qrcode.getHeight());

            // 2 CHANGE COLOR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            int qrColor = new Color(0, 0, 0).getRGB(); // QRCODE BLACK
            int bgColor = new Color(0, 0, 255).getRGB(); // BACK BLUE

            MatrixToImageConfig config = new MatrixToImageConfig(qrColor, bgColor);
            BufferedImage qrImage = MatrixToImageWriter.toBufferedImage(bitMatrix, config);

  
            File logoFile = new File(logoPath);
            if (!logoFile.exists()) {
                System.out.println("CANT FIND YOUR IMAGE.. !");
                return false;
            }
            BufferedImage logo = ImageIO.read(logoFile);

            int logoWidth = qrcode.getWidth() / 5;
            int logoHeight = qrcode.getHeight() / 5;

    
            int x = (qrcode.getWidth() - logoWidth) / 2;
            int y = (qrcode.getHeight() - logoHeight) / 2;

            Graphics2D g = qrImage.createGraphics();
            g.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
            g.drawImage(logo, x, y, logoWidth, logoHeight, null);
            g.dispose();


            File outputFile = new File(qrcode.getPath());
            ImageIO.write(qrImage, qrcode.getFormat(), outputFile);

            System.out.println("QRcode generated !!!");
            return outputFile.exists();
        } catch (Exception e) {
            System.out.println("ERROR : " + e.getMessage());
            return false;
        }
    }

    public static void main(String[] args) {
        QRcode qrcode = new QRcode();
        qrcode.setFormat("png");
        qrcode.setHeight(300);
        qrcode.setWidth(300);
        qrcode.setPath("./data/QRCODE26x.PNG");

        // Choisis le message du QR Code EXMPLE:
        // qrcode.setMessage("https://www.youtube.com/watch?v=3efwPrjwNVY");
        // qrcode.setMessage("salut..?"); 

        // 2 CHANGE LINK OF QRCODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!
        qrcode.setMessage("https://github.com/yanis26x");

        // 2 CHANGE LOGO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        String logoPath = "./data/sonic_logo.png";

        System.out.println(createQRcode(qrcode, logoPath));
    }
}
