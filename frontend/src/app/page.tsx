import Image from "next/image";
import styles from "./page.module.css";
import Pokeapi from "@/components/Pokeapi"

export default function Home() {
  return (
    <div>
      <main>
        <h1>My Dashboard</h1>
        <br></br>
        <Pokeapi />
      </main>
      <footer></footer>
    </div>
  );
}
