int generate_qr(const char *text, const char *output_file) {
    QRcode *qr = QRcode_encodeString(text, 0, QR_ECLEVEL_L, QR_MODE_8, 1);
    if (!qr) {
        printf("QR code generation failed!\n");
        return 1;
    }
    
    // Save as PNG (requires libpng, automatic with libqrencode)
    FILE *fp = fopen(output_file, "wb");
    if (!fp) {
        printf("Cannot create file: %s\n", output_file);
        QRcode_free(qr);
        return 1;
    }
    
    unsigned char *image = qr->data;
    int size = qr->width;

    int generate_qr(const char *text, const char *output_file) {
    QRcode *qr = QRcode_encodeString(text, 0, QR_ECLEVEL_L, QR_MODE_8, 1);
    if (!qr) {
        printf("QR code generation failed!\n");
        return 1;
    }
    
    // Save as PNG (requires libpng, automatic with libqrencode)
    FILE *fp = fopen(output_file, "wb");
    if (!fp) {
        printf("Cannot create file: %s\n", output_file);
        QRcode_free(qr);
        return 1;
    }
    
    unsigned char *image = qr->data;
    int size = qr->width;