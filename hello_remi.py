import remi.gui as gui
from remi import start, App


class HelloRemi(App):
    def main(self):
        container = gui.VBox(
            width=300,
            height=200,
            style={
                'margin': '50px auto',
                'text-align': 'center'
            }
        )

        self.lbl = gui.Label(
            'Tekan Tombol',
            style={
                'font-size': '20px',
                'margin': '10px'
            }
        )

        btn = gui.Button(
            'Klik Saya',
            height=40,
            width=150,
            style={
                'font-size': '16px',
                'margin': '10px auto'
            }
        )
        btn.onclick.do(self.on_click)

        # Susun komponen
        container.append(self.lbl)
        container.append(btn)

        return container

    def on_click(self, widget):
        self.lbl.set_text('Hello World')


if __name__ == "__main__":
    start(HelloRemi, address='127.0.0.1', port=8081, start_browser=True)
