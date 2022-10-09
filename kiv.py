Main = """
<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, None
    size: dp(48), dp(48)

Screen:
    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Download Songs and Videos from Youtube"
        right_action_items: [["folder-outline", lambda x: app.folder(), 'Choose a destiny folder']]


    Screen:
        name: "Home"    

        MDTextField:
            id: video
            text: ""
            hint_text: "Write the URL or the name here "
            pos_hint: {"center_x": 0.6, "center_y": 0.75}
            mode: "rectangle"
            size_hint_x: 0.4

        MDLabel:
            text: "Write the URL or the name of the video"
            theme_text_color: "Custom"
            pos_hint: {"center_x": 0.53, "center_y": 0.75}


        MDTextField:
            id: downloads
            hint_text: app.path
            text: ""
            pos_hint: {"center_x": 0.6, "center_y": 0.6}
            mode: "rectangle"
            hint_text_font_size: 1
            size_hint_x: 0.4
            on_text: app.setPath(self.text)

        MDLabel:
            text: "Choose a path to save your video at"
            theme_text_color: "Custom"
            pos_hint: {"center_x": 0.53, "center_y": 0.6}

        MDLabel:
            text: "High Quality"
            theme_text_color: "Custom"
            pos_hint: {"center_x": 0.53, "center_y": 0.4}

        MDLabel:
            text: "Low Quality"
            theme_text_color: "Custom"
            pos_hint: {"center_x": 0.53, "center_y": 0.33}     

        MDLabel:
            text: "Audio Only"
            theme_text_color: "Custom"
            pos_hint: {"center_x": 0.53, "center_y": 0.26}    

        Check:
            active: True
            pos_hint: {'center_x': .2, 'center_y': .4}
            on_press: app.option = 'high'

        Check:
            pos_hint: {'center_x': .2, 'center_y': .33}
            on_press: app.option = 'low'

        Check:
            pos_hint: {'center_x': .2, 'center_y': .26}
            on_press: app.option = 'audio'

        MDFillRoundFlatIconButton:
            id: download_button
            text: "Download"
            icon: "download"
            pos_hint: {'center_x': .5, 'center_y': .37}
            font_size: "20sp"
            md_bg_color: 30/255, 155/255, 227/255, 1
            text_color: 250/255, 250/255, 250/255, 1
            icon_color: 250/255, 250/255, 250/255, 1
            on_press: app.start()

        MDProgressBar:
            id: progress
            pos_hint: {"center_x": .51, "center_y": .14}
            size_hint_x: 0.4
            type: "indeterminate"
            running_duration: 0.7
            catching_duration: 0.7

        MDLabel:
            text: app.update
            theme_text_color: "Custom"
            pos_hint: {"center_y": 0.25}
            halign: 'center'
            font_size: "18sp"

        MDFillRoundFlatIconButton:
            id: open_button
            text: "Open"
            icon: "video-outline"
            pos_hint: {'center_x': .85, 'center_y': .18}
            font_size: "17sp"
            md_bg_color: 30/255, 155/255, 227/255, 1
            text_color: 250/255, 250/255, 250/255, 1
            icon_color: 250/255, 250/255, 250/255, 1
            on_press: app.startFile()
"""