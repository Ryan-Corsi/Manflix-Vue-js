<template>
  <div class="painel" style="color: white">
    
    <br/>
    <br/>
    <MoviesSection :movies="movies" />
    
    <br/>
    <br/>
    <MoviesSection :movies="movies" />
    
    <br/>
    <br/>
    <MoviesSection :movies="movies" />
  </div>
</template>

<script>
import MoviesSection from '../../components/MoviesSection'




export default {
  middleware: "auth",
  layout: "standard",
  components: {
    MoviesSection
  },
  data(){
    return {
      title: '131',
      
      movies:[
        { id: 1, banner: 'https://www.flixwatch.co/wp-content/uploads/80046726.jpg'},
        { id: 2, banner: 'https://th.bing.com/th/id/OIP.RneqFxGBvS0lu4xyBBZDcgHaEK?pid=ImgDet&rs=1'},
        { id: 3, banner: 'https://occ-0-2794-2219.1.nflxso.net/dnm/api/v6/E8vDc_W8CLv7-yMQu8KMEC7Rrr8/AAAABVV-pclDKQoTB9uZRSzmNwEkXV-4kXcg48CC2Bo25RDBmgqel0lO1kX3L1jD8GeNdiN-rkxi3mO6362QZbpqvSVplV9X.jpg?r=1f2'},
        { id: 4, banner: 'https://th.bing.com/th/id/R.308d0cd0ab85938df7913555d33224cb?rik=9hNLJ13KHQKR3w&pid=ImgRaw&r=0'},
        { id: 5, banner: 'https://th.bing.com/th/id/OIP.mib_N7xedk3vIhxqe5M51wHaEK?pid=ImgDet&rs=1'},
        { id: 6, banner: 'https://www.rockandpop.cl/wp-content/uploads/2019/08/netflix-saca-pecho-tras-el-exito-arrollador-de-la-casa-de-papel-en-todo-el-mundo.jpg'}

      ]
    }
  },
  methods: {
    
  },
};
</script>

<style lang="scss" scoped>
.painel {
  width: 198.1vh;
  height: 889px;
  background-color: black;
}
</style>
