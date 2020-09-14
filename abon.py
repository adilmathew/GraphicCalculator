import tkinter

window=tkinter.Tk()
window.geometry("300x300")
window.title("grpahics")
window.mainloop()

''' def save(self):
        self.c.postscript(file="circles.eps")
        self.image1 = Image.new("RGB", (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image1)
        self.draw.line(self.linee,tuple(self.black),self.penwidth)
        self.name="circles.png"
        self.image1.save(self.name)'''



'''ps = self.c.postscript(colormode='color')
         img = Image.open(io.BytesIO(ps.encode('utf-8')))
         img.save('/tmp/test.jpg')
         self.clear()
         cnv = getscreen().getcanvas()
         global hen
         ps = self.c.postscript(colormode='color')
         hen = filedialog.asksaveasfilename(defaultextension='.jpg')
         im = Image.open(io.BytesIO(ps.encode('utf-8')))
         im.save("adil" + '.jpg')'''
         '''self.train_data = []
         self.filename="adil.png"
         self.image1.save(self.filename)
         self.im = cv2.imread("adil.png")
         self.im2 = cv2.cvtColor(self.im, cv2.COLOR_BGR2GRAY)
         self.im2 = cv2.GaussianBlur(self.im2, (15, 15), 0)
         self.im2 = cv2.resize(self.im2, (28, 28), interpolation=cv2.INTER_AREA)
         self.thresh = 230
         self.im2_bw = cv2.threshold(self.im2, self.thresh, 255, cv2.THRESH_BINARY)[1]
         self.im2_ibw = (255 - self.im2_bw)
         self.im2_ibw = np.reshape(self.im2_ibw, (1, 28, 28))
         self.json_file = open('model_final.json', 'r')
         self.loaded_model_json = self.json_file.read()
         self.json_file.close()
         self.loaded_model = model_from_json(self.loaded_model_json)
         # load weights into new model
         self.loaded_model.load_weights("model_final.h5")
         self.train_data.append(self.im2_ibw)
         self.train_data[0] = np.array(self.train_data[0])
         self.train_data[0] = self.train_data[0].reshape(1, 1, 28, 28)
         self.result = self.loaded_model.predict_classes(self.train_data[0])

         if (self.result[0] == 10):
             self.s = self.s + '-'
         if (self.result[0] == 11):
             self.s = self.s + '+'
         if (self.result[0] == 12):
             self.s = self.s + '*'
         if (self.result[0] == 0):
             self.s = self.s + '0'
         if (self.result[0] == 1):
             self.s = self.s + '1'
         if (self.result[0] == 2):
             self.s = self.s + '2'
         if (self.result[0] == 3):
             self.s = self.s + '3'
         if (self.result[0] == 4):
             self.s = self.s + '4'
         if (self.result[0] == 5):
             self.s = self.s + '5'
         if (self.result[0] == 6):
             self.s = self.s + '6'
         if (self.result[0] == 7):
             self.s = self.s + '7'
         if (self.result[0] == 8):
             self.s = self.s + '8'
         if (self.result[0] == 9):
             self.s = self.s + '9'
         print(self.s)
         self.clear()'''

