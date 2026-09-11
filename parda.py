
    printf("QR code saved to: %s (Size: %dx%d)\n", output_file, size, size);
    return 0;
}

int open_link(const char *url) {
    printf("Opening link: %s\n", url);
