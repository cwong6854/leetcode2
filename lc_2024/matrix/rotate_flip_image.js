
/**
 * IBM Question 1: Rotate and Flip Image (October 9, 2024)
 * 
 * Conditions:
 * Given an n x n Image with only either 0s or 1s...
 * 
 * 1.) Rotate the Image clockwise, either by 0, 90, 180, or 270 degrees
 * 2.) Vertical Flip the Image (either 0 or 1 to determine flipping)
 * 3.) Horizontal Flip the Image (either 0 or 1 to determine flipping)
 * 
 * image - List[List[Number]]
 * rotation - Number
 * verticalFlip - Number
 * horizontalFlip - Number
 */

export function rotateFlipImage(image, rotation, verticalFlip, horizontalFlip) {
    // TODO
    let n = image.length;
    let left = 0;
    let right = n - 1;
    // Rotation
    if (rotation > 0) {
        while (left < right) {
            let top = left;
            let bottom = right;
            for (let i = 0; i < (right - left); i++) {
                let rotateImg = rotation;
                while (rotateImg > 0) {
                    let tmp = image[top][left + i];
                    image[top][left + i] = image[bottom - i][left]; // replace top left with bottom left column rightward
                    image[bottom - i][left] = image[bottom - i][right]; // replace bottom left with bottom right row upward
                    image[bottom - i][right] = image[top][right - i]; // replace bottom right with top right column leftward
                    image[top + i][right] = tmp; // top right with top left row downward
                    rotateImg -= 90;
                }
            }
            left += 1;
            right -= 1;
        }
    }

    // Vertical Flip
    if (verticalFlip === 1) {
        for (let col = 0; col < n; col ++) {
            let topRow = 0;
            let bottomRow = n - 1;
            while (topRow < bottomRow) {
                let tmp = image[topRow][col];
                image[topRow][col] = image[bottomRow][col];
                image[bottomRow][col] = tmp;
                topRow += 1;
                bottomRow -= 1;
            }
        }
    }
    // Horizontal Flip
    if (horizontalFlip === 1) {
        for (let i = 0; i < n; i++) {
            image[i].reverse();
        }
    }
    return image;
}