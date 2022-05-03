import os
import json

folderDir = "folder/"
# read every json file in the directory
for file in os.listdir(folderDir):
    xmin, ymin, xmax, ymax = 0, 0, 0, 0
    label = "15"
    list_of_points = []
    if file.endswith(".json"):
        # open the file
        with open(os.path.join(folderDir, file)) as json_file:
            # load the data
            data = json.load(json_file)
            # extract image hight and width
            image_width = 1 / data["imageWidth"]
            image_height = 1 / data["imageHeight"]
            # extract shapes
            shapes = data["shapes"]
            # extract point from shapes
            for shape in shapes:
                points = shape["points"]

                xmin = min(points[0][0], points[1][0])
                ymin = min(points[0][1], points[1][1])
                xmax = max(points[0][0], points[1][0])
                ymax = max(points[0][1], points[1][1])

                # convert to yolo format
                xcord = (xmin + xmax) / 2
                ycord = (ymin + ymax) / 2
                width = xmax - xmin
                height = ymax - ymin

                x = xcord * image_width
                y = ycord * image_height
                w = width * image_width
                h = height * image_height

                x = "{:.6f}".format(x)
                y = "{:.6f}".format(y)
                w = "{:.6f}".format(w)
                h = "{:.6f}".format(h)

                # append to list
                list_of_points.append([label, x, y, w, h])

            # save list_of_points file to txt
            with open(os.path.join(folderDir, file.replace(".json", ".txt")), "a") as f:
                for point in list_of_points:
                    for p in point:
                        f.write(str(p) + " ")
                    f.write("\n")
