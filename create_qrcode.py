#
# www.youtube.com/@mersthub_mentors
#

import qrcode
import os


def create_qrcode(input_url, output_dir, filename,
                  box_size=10, border=4, fill_color="red",
                  back_color="white"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border
    )
    qr.add_data(f"{input_url}")
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color,
                        back_color=back_color)
    img.save(f"{output_dir}/{filename}.png")


if __name__ == "__main__":
    create_qrcode(input_url="https://www.youtube.com/@mersthub_mentors",
                  output_dir=".",
                  filename="my_qrcode",
                  box_size=10,
                  border=4,
                  fill_color="Orange",
                  back_color="white")
