import qrcode
import PySimpleGUI as pi
import os

# Define the layout of the GUI window
layout = [
    [pi.Text('Enter URL or text:'), pi.InputText(key='text')],
    [pi.Text('Select QR code size:'), pi.Spin(values=list(range(1, 21)),key='size',initial_value=8,size=(5,10))],
    [pi.Text('Select QR code color:'),pi.Radio('Black', "COLOR", default=True, key='color_black'), pi.Radio('Blue', "COLOR", key='color_blue')],
    [pi.Button('Generate QR Code'), pi.Cancel()],
    [pi.Image(key='image')]
]

# Create the window
window = pi.Window('QR Code Generator', layout,background_color='teal')

# Event loop to process "Generate QR Code" button clicks
while True:
    event, values = window.read()
    if event == pi.WINDOW_CLOSED or event =='Cancel':
        break

    else:
        # Get the user input and generate the QR code image
       
        qr = qrcode.QRCode(version=1, box_size=values['size'], border=4)
        qr.add_data(values['text'])
        qr.make(fit=True)

        # Generate the QR code image
        img = qr.make_image(fill_color='black' if values['color_black'] else 'blue', back_color='white')
        # Save the QR code image to a file
        img_file = 'qrcodg' + '.png'
        path = os.path.join(os.getcwd(),img_file)
        img.save(path)

        # Update the window to display the QR code image
        window['image'].update(filename=path)

# Close the GUI window
window.close()
