# Album Wall Art

My first stab at computational art -- a piece for my wall. I just want to throw a bunch of random computational tools at a single problem: make a cool piece of art that involves all the albums I've listened to this year & can grow as I listen to more. I'm thinking CNNs, graph algorithms, GANs for style transfer, everything.

## Steps

1. Import images of album covers from a list of (album names, artist) pairs.
  - Use Google Image API and Python

2. Figure out what pieces of art I like
  - Tom Scott's video => compare pairs of art to figure out a ranking of art
  - Train CNN to learn this art => ranking function
    - Need to standardize sizes of art
  - Potentially train GAN to generate art that I like?

3. Generate layouts of images
  - Increase size of albums based on their importance, using similar ranking mechanism as before
  - Connect albums with a cool link
  - Experiment with grid, overlapping, & blended layout of images

4. Print!
  - Either print out poster or individual images
