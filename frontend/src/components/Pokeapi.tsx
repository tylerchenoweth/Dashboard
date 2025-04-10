"use client";

// import { useState, useEffect } from "react";

// type Pokemon = {
//   name: string;
//   image: string;
//   order: number;
//   type: string;
//   weight: number|string;
//   gif: string;
// };

// export default function Pokemon() {
//   const [pokemon, setPokemon] = useState<Pokemon | null>(null);

  // useEffect(() => {
  //   fetch("http://localhost:8000/pokeapi/random")
  //     .then((res) => res.json())
  //     .then((data) => setPokemon(data))
  //     .catch((error) => console.error("Error fetching data:", error));
  // }, []);



//   useEffect(() => {
//     const fetchData = async () => {
//         const response = await fetch("http://localhost:8000/pokeapi/random");
//         const data = await response.json();
//         setPokemon(data);
//     };

//     fetchData(); // Fetch on load
//     const interval = setInterval(fetchData, 10000); // Fetch every 60 seconds

//     return () => clearInterval(interval); // Cleanup on unmount
// }, []);







// useEffect(() => {
//   const fetchData = async () => {
//       try {
//           const response = await fetch("http://localhost:8000/pokeapi/random");
//           const data = await response.json();

//           // Update only if the fetched Pokémon is different
//           setPokemon((prevPokemon) => {
//               return prevPokemon?.order !== data.order ? data : prevPokemon;
//           });
//       } catch (error) {
//           console.error("Error fetching data:", error);
//       }
//   };

//   fetchData(); // Fetch immediately on load

//   const interval = setInterval(fetchData, 10000); // Poll every 10 seconds

//   return () => clearInterval(interval); // Cleanup on unmount
// }, []);






//   if (!pokemon) return <p>Loading...</p>;

//   return (
//     <div>
//       <h2>{pokemon.name}</h2>
//       <br></br>
//       <img src={pokemon.gif} alt={pokemon.name} />
//       <br></br><br></br>
//       <p><b>Pokedex #: </b>{pokemon.order}</p>
//       <p><b>Type: </b>{pokemon.type}</p>
//       <p><b>Weight: </b>{pokemon.weight} lbs</p>
//     </div>
//   );
// }





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



import { useEffect, useState } from "react";

const API_URL = "http://localhost:8000/pokeapi/randomoriginal";

export default function DataDisplay() {
  const [data, setData] = useState(null);

  let counter = 0;

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(API_URL);
        if (response.ok) {
          const result = await response.json();
          setData(result);
          counter += 1;
          console.log("CHECKING BACKEND!-----", counter);
        }
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData(); // Initial fetch
    const interval = setInterval(fetchData, 10000); // Fetch every 10 seconds
    console.log("CHECKING BACKEND!");
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h1>Latest Data</h1>
      {data ? <pre>{JSON.stringify(data, null, 2)}</pre> : <p>Loading...</p>}
    </div>
  );
}

