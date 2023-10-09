#include <iostream>
#include <cstring>
#include <cstdlib>  // For strtol
#include <htslib/sam.h>

int main(int argc, char *argv[]) {
    if (argc != 4) {
        std::cerr << "Usage: " << argv[0] << " <input.bam> <output.bam> <threshold>" << std::endl;
        return 1;
    }

    const char *input_bam = argv[1];
    const char *output_bam = argv[2];
    long threshold = std::strtol(argv[3], nullptr, 10);  // Convert threshold argument to long

    samFile *in = sam_open(input_bam, "r");

    if (in == NULL) {
        std::cerr << "Error opening input BAM file: " << input_bam << std::endl;
        return 1;
    }

    bam_hdr_t *header = sam_hdr_read(in);
    samFile *out = sam_open(output_bam, "wb");

    if (out == NULL) {
        std::cerr << "Error opening output BAM file: " << output_bam << std::endl;
        return 1;
    }

    sam_hdr_write(out, header) __attribute__((warn_unused_result)); // Suppress warning
    bam1_t *record = bam_init1();

    while (sam_read1(in, header, record) >= 0) {
        uint32_t as = 0, xs = 0;

        // Extract AS and XS fields from the BAM record
        uint8_t *as_ptr = bam_aux_get(record, "AS");
        uint8_t *xs_ptr = bam_aux_get(record, "XS");

        if (as_ptr != NULL) as = bam_aux2i(as_ptr);
        if (xs_ptr != NULL) xs = bam_aux2i(xs_ptr);

        int as_minus_xs = as - xs;

        if (as_minus_xs >= threshold) {
            sam_write1(out, header, record) __attribute__((warn_unused_result)); // Suppress warning
        }
    }

    bam_destroy1(record);
    bam_hdr_destroy(header);
    sam_close(in);
    sam_close(out);

    return 0;
}
