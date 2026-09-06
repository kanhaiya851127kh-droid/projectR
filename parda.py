
    printf("QR code saved to: %s (Size: %dx%d)\n", output_file, size, size);
    return 0;
}

int open_link(const char *url) {
    printf("Opening link: %s\n", url);
    
#ifdef _WIN32
    char command[512];
    snprintf(command, sizeof(command), "start \"\" \"%s\"", url);
    system(command);
#elif __APPLE__
    char command[512];
    snprintf(command, sizeof(command), "open \"%s\"", url);
    system(command);
#else
    char command[512];
    snprintf(command, sizeof(command), "xdg-open \"%s\" 2>/dev/null || sensible-browser \"%s\"", url, url);
    int result = system(command);
    if (result != 0) {
        printf("Failed to open browser. Please open manually: %s\n", url);
    }

