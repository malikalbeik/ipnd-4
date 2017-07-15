import fresh_tomatoes
import media

the_godfather = media.Movie("The godfather",
                            "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                            "http://imgsrc.allposters.com/img/print/posters/the-godfather_a-G-1635808-0.jpg",
                            "https://youtu.be/sY1S34973zA")

star_wars = media.Movie("Star wars",
                        "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a wookiee and two droids to save the galaxy from the Empire's world-destroying battle-station, while also attempting to rescue Princess Leia from the evil Darth Vader.",
                        "http://t3.gstatic.com/images?q=tbn:ANd9GcTqRzbG-zvWPx5khd-1D9st1B7FYEq71Gbd2UdaPnrWPwVvY2PX",
                        "https://youtu.be/vP_1T4ilm8M")

titanic = media.Movie("Titanic",
                      "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
                      "https://www.movieposter.com/posters/archive/main/142/MPW-71146",
                      "https://youtu.be/2e-eXJ6HgkQ")

despicable_me = media.Movie("Despicable Me",
                            "A man who delights in all things wicked, supervillain Gru (Steve Carell) hatches a plan to steal the moon.",
                            "http://t2.gstatic.com/images?q=tbn:ANd9GcStk75A_FacVc2kXVb8vdTAU6x-fmRjV2X0-6yxHF5iksQmzKwB",
                            "https://youtu.be/TZkAcKCFIVo")

transformers = media.Movie("Transformers",
                           "The fate of humanity is at stake when two races of robots, the good Autobots and the villainous Decepticons, bring their war to Earth.",
                           "http://www.gstatic.com/tv/thumb/movieposters/159729/p159729_p_v8_ar.jpg",
                           "https://youtu.be/UxI_JI6chas")

irobot = media.Movie("I, robot",
                     "In 2035, highly intelligent robots fill public service positions throughout the world, operating under three rules to keep humans safe.",
                     "http://www.gstatic.com/tv/thumb/movieposters/34586/p34586_p_v8_ap.jpg",
                     "https://youtu.be/rL6RRIOZyCM")

movies = [the_godfather, star_wars, titanic,
          despicable_me, transformers, irobot]

fresh_tomatoes.open_movies_page(movies)
