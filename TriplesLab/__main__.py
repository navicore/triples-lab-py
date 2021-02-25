"""This module serves as the entry point of TriplesLab."""
import rdflib


def main():
    # create a Graph
    g = rdflib.Graph()

    g.parse("file:data/Brick.n3", format="n3")

    # loop through each triple in the graph (subj, pred, obj)
    for subj, pred, obj in g:
        # check if there is at least one triple in the Graph
        if (subj, pred, obj) not in g:
            raise Exception("It better be!")

    # print the number of "triples" in the Graph
    print("graph has {} statements?".format(len(g)))
    # prints graph has 86 statements.
    #
    # # print out the entire Graph in the RDF Turtle format
    # print(g.serialize(format="turtle").decode("utf-8"))


if __name__ == '__main__':
    main()
