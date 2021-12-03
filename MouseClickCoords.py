import cv2
import numpy as np

MAXWIDTHTOKEEP = 2592
MAXHEIGHTTOKEEP = 1944
imgs = []
windowCount = 0

caseStages = []

posList = []
def onMouse(event, x, y, flags, param):
   global posList
   if event == cv2.EVENT_LBUTTONDOWN:
     print("bgr: ", imgs[param][y, x], "hsv: ", cv2.cvtColor(imgs[param], cv2.COLOR_BGR2HSV)[y, x])

def displayImg(img, name=""):
   global windowCount
   if not name:
      name = "customWindow"+str(windowCount)
      windowCount += 1
   #cv2.imshow(name, img)


def normalizeImg(img):
   r, g, b = cv2.split(img)
   mask1=r<8
   mask2=g<8
   mask3=b<8
   mask = mask1
   mask = mask & mask2
   mask = mask & mask3
   img[mask] = (0, 0, 0)
   return img

def normalizeImgSize(img):
  width = np.min((img.shape[1], MAXWIDTHTOKEEP))
  height = np.min((img.shape[0], MAXHEIGHTTOKEEP))
  resizedImg = cv2.resize(img, (width, height), interpolation = cv2.INTER_AREA)
  return resizedImg

def resizeImg(img, percent): 
  width = int(img.shape[1] * percent / 100)
  height = int(img.shape[0] * percent / 100)
  dim = (width, height)
  resizedImg = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
  #print ("size is ", dim)
  return resizedImg

def claheProcessAndEnhance(img):
   clahe = cv2.createCLAHE(clipLimit=9.0, tileGridSize=(8,8))
   y, u, v = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2YUV))
   enhancedY = clahe.apply(y)
   claheRed = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
   v = claheRed.apply(v)
   #v = claheRed.apply(v)
   enhancedImg = cv2.merge((enhancedY, u, v))

   enhancedImg = cv2.cvtColor(enhancedImg, cv2.COLOR_YUV2BGR)
   return enhancedImg

def readOriginalAndWriteEnhanced(id):
   id = str(id)   
   img = cv2.imread(r"C:/Users/indra094/Downloads/TestSet/train/"+str(id)+"_right.jpeg", 1)

   img = normalizeImgSize(img)
   #img = resizeImg(img3, 20)
   enhancedImg = claheProcessAndEnhance(img)
   cv2.imwrite("ResultImages/enhanced"+id+".jpeg", enhancedImg)
   cv2.imwrite("ResultImages/orig"+id+".jpeg", img)

def displayImgProperly(idxList):
   for i in range(len(idxList)):
      imgs[i] = normalizeImgSize(imgs[i])
      imgs[i] = resizeImg(imgs[i], 20)
      displayImg(imgs[i], "origImage"+str(i))

def dumpImage(img, id, name):
   cv2.imwrite("ResultImages/"+name+str(id)+".jpeg", img)

def adjustGreenPatches(img):
   r, g, b = cv2.split(img)
   mask = (2*g - (b+r)) >30
   g[mask] -= 15
   b[mask] += 15
   r[mask] += 15
   img = cv2.merge((r, g, b))
   return img

def displayEnhancedImgsProperly(idxList):
   for i in range(len(idxList)):
      img = claheProcessAndEnhance(imgs[i])
      #img = adjustGreenPatches(img)
      imgs.append(img)
      #imgs[len(idxList)+i] = resizeImg(imgs[len(idxList)+i], 20)
      #displayImg(img, "enhanced"+str(i))
      dumpImage(img, idxList[i], "enhancedWell")
      
def setUpWindows(idxList):
   for i in range(3*len(idxList)):
      windows[i]="Window"+str(i) 

def setupMouseClicks(idxList):
   for i in range(3*len(idxList)):
      cv2.setMouseCallback(windows[i], onMouse, param=((i)))  

def readImages(idxList):
   for i in range(len(idxList)):
      imgs.append(normalizeImg(cv2.imread(r"C:/Users/indra094/Downloads/TestSet/train/"+str(idxList[i])+"_left.jpeg", 1)))
      
def extract_bv(image):

  b,green_fundus,r = cv2.split(image)
  clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
  contrast_enhanced_green_fundus = clahe.apply(green_fundus)
  enhancedR = clahe.apply(r)
  enhancedB = clahe.apply(b)
  enhancedImg = cv2.merge((b, contrast_enhanced_green_fundus, r))
  #displayImg(cv2.merge((b, contrast_enhanced_green_fundus, enhancedR)))
  #displayImg(contrast_enhanced_green_fundus)
  
	# applying alternate sequential filtering (3 times closing opening)
  r1 = cv2.morphologyEx(contrast_enhanced_green_fundus, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)), iterations = 1)
  #displayImg(r1)
  R1 = cv2.morphologyEx(r1, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)), iterations = 1)
  #displayImg(R1)
  r2 = cv2.morphologyEx(R1, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11)), iterations = 1)
  #displayImg(r2)
  R2 = cv2.morphologyEx(r2, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11)), iterations = 1)
  #displayImg(R2)
  r3 = cv2.morphologyEx(R2, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(23,23)), iterations = 1)
  #displayImg(r3)
  R3 = cv2.morphologyEx(r3, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(23,23)), iterations = 1)	
  #displayImg(R3)
  f4 = cv2.subtract(R3,contrast_enhanced_green_fundus)
  #displayImg(f4)
  f5 = clahe.apply(f4)		
  #displayImg(f5)
  
  # removing very small contours through area parameter noise removal
  ret,f6 = cv2.threshold(f5,15,255,cv2.THRESH_BINARY)
  #displayImg(f6)
  mask = np.ones(f5.shape[:2], dtype="uint8") * 255	
  contours, hierarchy = cv2.findContours(f6.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
  for cnt in contours:
    if cv2.contourArea(cnt) <= 20:
      cv2.drawContours(mask, [cnt], -1, 0, -1)			
  #displayImg(mask)    
  #displayImg(f5)
  im = cv2.bitwise_and(f5, f5, mask=mask)
  #displayImg(im, "IM")
  ret,fin = cv2.threshold(im,15,255,cv2.THRESH_BINARY_INV)			
  #displayImg(fin, "fin")
  #newfin = cv2.morphologyEx(fin, cv2.MORPH_open, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3)), iterations = 1)	
  newfin = cv2.dilate(fin, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(1,1)), iterations=1)
  newfin = cv2.erode(newfin, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2)), iterations=1)	
  #displayImg(newfin,"newfin")

  # removing blobs of unwanted bigger chunks taking in consideration they are not straight lines like blood
  #vessels and also in an interval of area
  fundus_eroded = cv2.bitwise_not(newfin)
  #displayImg(fundus_eroded,"fundus_eroded")
  xmask = np.ones(fundus_eroded.shape[:2], dtype="uint8") * 255
  
  xcontours, xhierarchy = cv2.findContours(fundus_eroded.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)	
  for cnt in xcontours:
    shape = "unidentified"
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.04 * peri, False)   				
    if len(approx) > 4 and cv2.contourArea(cnt) <= 3000:# and cv2.contourArea(cnt) >= 100:
      shape = "circle"
    else:
      shape = "veins"
    if(shape=="circle"):
      cv2.drawContours(xmask, [cnt], -1, 0, -1)	
  
      
  finimage = cv2.bitwise_and(fundus_eroded,fundus_eroded,mask=xmask)
  #displayImg(xmask,"xmask")
  #displayImg(finimage,"finimage")
  blood_vessels = cv2.bitwise_not(finimage)
  blood_vessels = cv2.morphologyEx(blood_vessels, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(4,4)), iterations = 1)
  rect = cv2.rectangle(blood_vessels, (0, 0), (blood_vessels.shape[1], blood_vessels.shape[0]), 255, 5)
  #colorVessels = cv2.cvtColor(rect, cv2.COLOR_GRAY2BGR)
  areaSum = 0
  xcontours, xhierarchy = cv2.findContours(cv2.bitwise_not(rect),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)	
  for cnt in xcontours:
    area = cv2.contourArea(cnt)
    areaSum += area
  
  #cv2.drawContours(colorVessels, xcontours, -1, (0,255,0), 3)	
  #displayImg(colorVessels,"colorVessels")
  #print(areaSum, len(xcontours))
  
  return areaSum, blood_vessels, enhancedImg

enhancedVeins = []

def displayVeinsFromEnhancedImages(idxList):
   for i in range(len(idxList)):
      img = extract_bv(imgs[len(idxList)+i])
      enhancedVeins.append(img)
      #dumpImage(img, idxList[i], "veins")
      #img = resizeImg(img, 20)
      #displayImg(enhancedVeins)

      
      
def detectExudates(img, i):
      bwImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      mask = veins[i]==0
      
      #img = imgs[len(idxList)+i].copy()
      img[mask] = (0,0,0)

      clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(8,8))
      b,green_fundus,r = cv2.split(img)
      contrast_enhanced_green_fundus = clahe.apply(green_fundus)
      enhancedR = clahe.apply(r)
      enhancedB = clahe.apply(b)
      newImg = (cv2.merge((b, contrast_enhanced_green_fundus, enhancedR)))
      displayImg(newImg)
      
      r, g, b = cv2.split(newImg)
      maxR = np.max(r)
      meanR = np.mean(r)
      maxG = np.max(g)
      meanG = np.mean(g)
      #displayImg(bwImage)
      rThreshVal = (maxR + meanR)/2
      _, rThresh = cv2.threshold(r, rThreshVal, 255, cv2.THRESH_BINARY)
      gThreshVal = (maxG + meanG)/2
      _, gThresh = cv2.threshold(g, gThreshVal, 255, cv2.THRESH_BINARY)

      _, thresh = cv2.threshold(bwImage, 100,255,cv2.THRESH_BINARY)
      mask = (cv2.bitwise_and(rThresh, gThresh)  == 0)
      #mask2 = (ythresh2==0)
      img2 = img.copy()
      img2[mask] = (0, 0, 0)
      kernel = np.ones((2, 2), np.uint8)
  
      # Using cv2.erode() method 
      img2 = cv2.erode(img2, kernel)
      img2 = cv2.erode(img2, kernel)

      kernel2 = np.ones((15, 15), np.uint8)
      img2 = cv2.dilate(img2, kernel2)

      img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
      mask = img2 >0
      img2[mask] = 255

      contours, hierarchy = cv2.findContours(img2,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
      exudateCount = -1
      xmask = np.ones(img2.shape[:2], dtype="uint8") * 255
      for cnt in contours:
         #print (cv2.contourArea(cnt))
         if 6<cv2.contourArea(cnt) <3000:
            exudateCount+=1
            #cv2.drawContours(img2, cnt, -1, (0, 255, 0), 3)
            #print (cv2.contourArea(cnt))

         if cv2.contourArea(cnt)<6 or cv2.contourArea(cnt)>3000:
            cv2.drawContours(xmask, [cnt], -1, 0, -1)
         
      #bwImage[mask2] = 0
      
      img2 = cv2.bitwise_and(img2, img2,mask=xmask)
      #img2 = cv2.bitwise_not(img2)
      #dumpImage(img2, 3, "exu")            
      
      newMat = np.zeros_like(bwImage)
      
      #print (len(thresh))
      #displayImg(img2, "img2")
      

      return exudateCount, cv2.bitwise_not(img2)
      #displayImg(ythresh)
      #displayImg(ythresh2)


def detectHaemorrages(image):

      #bwImage = cv2.cvtColor(imgs[len(idxList)+i], cv2.COLOR_BGR2GRAY)
      b,green_fundus,r = cv2.split(image)
      clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
      contrast_enhanced_green_fundus = clahe.apply(green_fundus)
      enhancedR = clahe.apply(r)
      enhancedB = clahe.apply(b)
  #displayImg(cv2.merge((b, contrast_enhanced_green_fundus, enhancedR)))
  #displayImg(contrast_enhanced_green_fundus)
  
	# applying alternate sequential filtering (3 times closing opening)
      r1 = cv2.morphologyEx(contrast_enhanced_green_fundus, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)), iterations = 1)
  #displayImg(r1)
      R1 = cv2.morphologyEx(r1, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)), iterations = 1)
  #displayImg(R1)
      r2 = cv2.morphologyEx(R1, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11)), iterations = 1)
  #displayImg(r2)
      R2 = cv2.morphologyEx(r2, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11)), iterations = 1)
  #displayImg(R2)
      r3 = cv2.morphologyEx(R2, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(23,23)), iterations = 1)
  #displayImg(r3)
      R3 = cv2.morphologyEx(r3, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(23,23)), iterations = 1)	
  #displayImg(R3)
      f4 = cv2.subtract(R3,contrast_enhanced_green_fundus)
  #displayImg(f4)
      f5 = clahe.apply(f4)		
  #displayImg(f5)
  
  # removing very small contours through area parameter noise removal
      ret,f6 = cv2.threshold(f5,15,255,cv2.THRESH_BINARY)
  #displayImg(f6)
      mask = np.ones(f5.shape[:2], dtype="uint8") * 255	
      contours, hierarchy = cv2.findContours(f6.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
      for cnt in contours:
         if cv2.contourArea(cnt) <= 20:
            cv2.drawContours(mask, [cnt], -1, 0, -1)			
  #displayImg(mask)    
  #displayImg(f5)
      
      #_, f5Thresh = cv2.threshold(f5, 100,255,cv2.THRESH_BINARY)

      im = cv2.bitwise_and(f5, f5, mask=mask)
  #displayImg(im)
      ret,fin = cv2.threshold(im,15,255,cv2.THRESH_BINARY_INV)			
  #displayImg(fin)
      newfin = cv2.erode(fin, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3)), iterations=1)	
  #displayImg(newfin)

  # removing blobs of unwanted bigger chunks taking in consideration they are not straight lines like blood
  #vessels and also in an interval of area
      fundus_eroded = cv2.bitwise_not(newfin)
  #displayImg(fundus_eroded)
      xmask = np.ones(fundus_eroded.shape[:2], dtype="uint8") * 255
  
      xcontours, xhierarchy = cv2.findContours(fundus_eroded.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)	
      for cnt in xcontours:
         shape = "unidentified"
         peri = cv2.arcLength(cnt, True)
         approx = cv2.approxPolyDP(cnt, 0.04 * peri, False)   				
         if len(approx) > 4 and cv2.contourArea(cnt) <= 3000:# and cv2.contourArea(cnt) >= 100:
            shape = "circle"	
         else:
            shape = "veins"
         if(shape=="circle"):
            cv2.drawContours(xmask, [cnt], -1, 0, -1)
  #displayImg(xmask)
      
      finimage = cv2.bitwise_and(fundus_eroded,fundus_eroded,mask=xmask)

      f5Copy = f5.copy()
      mask2 = f5Copy > 20
      f5Copy[mask2] = 255
      #displayImg(f5Copy, "f5Copy")
      displayImg(f6, "f6")
      mask3 = finimage == 255
      haemAndNoiseImg = f5Copy.copy()
      haemAndNoiseImg[mask3] = 0
      #haemAndNoiseImg = cv2.erode(haemAndNoiseImg, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2)), iterations=1)	
      
      haemAndNoiseImg = cv2.bitwise_not(haemAndNoiseImg)
      mask = haemAndNoiseImg > 0
      haemAndNoiseImg[mask] = 255
 
      haemAndNoiseImg = cv2.morphologyEx(haemAndNoiseImg, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2)), iterations = 1)
      haemAndNoiseImg = cv2.morphologyEx(haemAndNoiseImg, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2)), iterations = 1)
      haemAndNoiseImg = cv2.morphologyEx(haemAndNoiseImg, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(1,1)), iterations = 1)
      haemAndNoiseImg = cv2.morphologyEx(haemAndNoiseImg, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(1,1)), iterations = 1)
      kernel = np.ones((2, 2), np.uint8)
      haemAndNoiseImg = cv2.erode(haemAndNoiseImg, kernel)
      haemAndNoiseImg = cv2.rectangle(haemAndNoiseImg, (0, 0), (haemAndNoiseImg.shape[1], haemAndNoiseImg.shape[0]), 255, 3)

      #displayImg(haemAndNoiseImg, "haemAndNoiseImgbef") 
      # Using cv2.erode() method 
      #haemAndNoiseImg = cv2.erode(haemAndNoiseImg, kernel)
      xcontours, xhierarchy = cv2.findContours(cv2.bitwise_not(haemAndNoiseImg),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
      newConts = []
      xmask = np.ones(haemAndNoiseImg.shape[:2], dtype="uint8") * 255
      micro=0
      haem=0
      #print (len(xcontours))
      for cnt in xcontours:
         approx = cv2.approxPolyDP(cnt, 0.04 * peri, False)   				
         peri = cv2.arcLength(approx, True)
         contourArea = cv2.contourArea(cnt)
         if contourArea<7 or contourArea>200:
            cv2.drawContours(xmask, [cnt], -1, 0, -1)
         elif contourArea<10:
            micro+=1
         else:
            haem +=1

      haemAndNoiseImg = cv2.bitwise_and(cv2.bitwise_not(haemAndNoiseImg),cv2.bitwise_not(haemAndNoiseImg),mask=xmask)
         
      #displayImg(cv2.bitwise_not(haemAndNoiseImg), "haemAndNoise")
      #dumpImage(cv2.bitwise_not(haemAndNoiseImg), idxList[i], "haemAndNoise")
      return micro, haem, cv2.bitwise_not(haemAndNoiseImg)


veins = []

def displayVeinsFromOriginalImages(idxList):
   for i in range(len(idxList)):
      areaSum, img, enh = extract_bv(imgs[i])
      if areaSum > 10000:
         caseStages[i]+=1

      displayImg(img, "BloodVessels"+str(i))
      veins.append(img)
      dumpImage(img, idxList[i], "veins")
      dumpImage(enh, idxList[i], "enhanced")
      #img = resizeImg(img, 20)
      #cv2.imshow(windows[2*len(idxList)+i], img)
  
windows = {}
idxList = [10, 36, 25, 21, 217, 294, 326, 367]#, 405, 406, 458]#[328, 352, 391, 458, 509, 531]#
#idxList.append(16)#, 294)#, 326, 367, 405)#(294, 217, 326, 367, 405)
#idxList.append(294)#10, 49, 99, 16, 217)

for i in range(len(idxList)):
   caseStages.append(0)

readImages(idxList)
setUpWindows(idxList)
displayImgProperly(idxList)
displayEnhancedImgsProperly(idxList)

displayVeinsFromOriginalImages(idxList)

for i in range(len(idxList)):
   exudateCount, img = detectExudates(imgs[len(idxList)+i], i)
   displayImg(img,"exudatesImg"+str(i))
   dumpImage(img, idxList[i], "exudates")
   if exudateCount > 3:
      caseStages[i]+=1

for i in range(len(idxList)):
   micro, haems, retImg = detectHaemorrages(imgs[i])
   displayImg(retImg,"HaemImg"+str(i))
   dumpImage(retImg, idxList[i], "haemAndMA")
   if haems > 2:
      caseStages[i]+=2
   elif micro > 4:
      caseStages[i]+=1

print (caseStages)
   
#setupMouseClicks(idxList)

readOriginalAndWriteEnhanced(49)

k = cv2.waitKey(0) & 0xff
cv2.destroyAllWindows()         
         
#print(posList[0])
