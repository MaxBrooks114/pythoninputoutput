import pickle

# imelda = ('More Mayhem', 'IMelda May', '2011', ((1, "pulling the rug"), (2, 'psycho'), (3, 'mayhem'), (4, 'kentish town waltz')))

# with open("imelda.pickle", "wb") as pickle_file:
#     pickle.dump(imelda, pickle_file)

with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)


print(imelda2)


with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)
    pickle.dump()