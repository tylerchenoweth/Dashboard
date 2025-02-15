"use client";

import { useState, useEffect } from "react";

type Pokemon = {
  name: string;
  image: string;
  order: number;
  type: string;
  weight: number|string;
  gif: string;
};

export default function Pokemon() {
  const [pokemon, setPokemon] = useState<Pokemon | null>(null);

  useEffect(() => {
    fetch("http://localhost:8000/pokeapi/")
      .then((res) => res.json())
      .then((data) => setPokemon(data))
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  if (!pokemon) return <p>Loading...</p>;

  return (
    <div>
      <h2>{pokemon.name}</h2>
      <br></br>
      <img src={pokemon.gif} alt={pokemon.name} />
      <br></br><br></br>
      <p><b>Pokedex #: </b>{pokemon.order}</p>
      <p><b>Type: </b>{pokemon.type}</p>
      <p><b>Weight: </b>{pokemon.weight} lbs</p>
    </div>
  );
}





// #######################################################
// #                                                     #
// #   BELOW IS THE CODE FOR THE SERVER SIDE RENDERING   #
// #                                                     #
// #######################################################



// import { GetServerSideProps } from "next";

// type Pokemon = {
//   name: string;
//   image: string;
//   order: number;
//   type: string;
//   weight: number;
//   gif: string;
// };

// export default async function PokemonPage() {
//   const res = await fetch("http://localhost:8000/pokeapi", { cache: "no-store" });
//   const pokemon = await res.json();

//   return (
//     <div>
//       <h2>{pokemon.name}</h2>
//       <br></br>
//       <img src={pokemon.gif} alt={pokemon.name} />
//       <br></br><br></br>
//       <p><b>ID: </b>{pokemon.order}</p>
//       <p><b>Type: </b>{pokemon.type}</p>
//       <p><b>Weight: </b>{pokemon.weight} lbs</p>
//     </div>
//   );
// }




