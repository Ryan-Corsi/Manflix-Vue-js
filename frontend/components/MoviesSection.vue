<template>
  <div>
    <h1>Filmes e Documentários</h1>
    <br/>
    <br/>
    <Carousel :per-page="6">
      <Slide v-for="movie in movies" :key="movie.id">
        <img
          :src="movie.banner"
          
        />
        
      </Slide>
    </Carousel>
  </div>
</template>


<script>
import { Carousel, Slide } from "vue-carousel";

export default {
  components: {
    Carousel,
    Slide
  },

  props: {
    movies: {
      type: Array,
    },
  },
};
</script>
