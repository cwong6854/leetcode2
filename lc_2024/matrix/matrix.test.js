import { rotateFlipImage } from "./rotate_flip_image";
// rotate_flip_image.js
test('image rotate 270 clockwise and horizontal flip', () => {
    var test = [[1,0,0], [0,0,0], [0,0,0]];
    let result = rotateFlipImage(test, 270, 0, 1);
    let actual = [[0,0,0],[0,0,0],[0,0,1]];
    expect(result).toEqual(actual);
    }
)
test('image rotate 90 clockwise, vertical flip, and horizontal flip', () => {
    var test = [[1,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]];
    let result = rotateFlipImage(test, 180, 1, 1);
    let actual = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]];
    expect(result).toEqual(actual);
    }
)
