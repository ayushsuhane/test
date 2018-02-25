from due import due,Doi,BibTeX
due.cite(BibTeX("""
           @article{mynicearticle,
           title={A very cool paper},
           author={Happy, Author and Lucky, Author},
           journal={The Journal of Serendipitous Discoveries}
           }
           """), 
           description="Solves all your problems", path="randomtests")


