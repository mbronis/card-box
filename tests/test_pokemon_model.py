# from src.model import Card, Encyclopedia
# from src.pokemons import PokemonCard, PokemonType


# def get_pokemons():
#     pikachu = PokemonCard("pikachu", (PokemonType.ELECTRIC), (PokemonType.GRASS), 50)
#     bulbasaur = PokemonCard("bulbasaur", (PokemonType.FIRE), (PokemonType.WATER), 100)
#     ivysaur = PokemonCard("ivysaur", (PokemonType.FIRE), (PokemonType.WATER), 200, bulbasaur)

#     return pikachu, bulbasaur, ivysaur


# def test_creating_encyclopedia_fails_on_wrong_card_type():
#     pikachu, _ = get_pokemons()


#     poke_dex = Encyclopedia(card_type=Card)
#     with
#     poke_dex.add({pikachu})

#     assert pikachu in poke_dex
#     assert len(poke_dex) == 3


# def test_creating_encyclopedia():
#     pikachu, bulbasaur, ivysaur = get_pokemons()

#     poke_dex = Encyclopedia(card_type=PokemonCard)
#     poke_dex.add({pikachu, bulbasaur, ivysaur})

#     assert pikachu in poke_dex
#     assert len(poke_dex) == 3
