<template>
  <div class="">
    <div class="row">
      <div class="col-md-12 text-center">
        <bar-chart :data="barData.most_common_words" title="Most Command Words" label="Frequency"
        xtitle="Frequency" ytitle="Words"></bar-chart>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import axios from "axios"

export default {
  name: 'home',
  components: {

  },


  data() {
      return {
          barData : [],
      }
  },
  methods: {
      getData(){
        axios.get("http://127.0.0.1:8000/most-common-tweet-words/")
        .then(res =>(this.barData = res.data))
        .catch(err => console.log(err));
      }
  },
  created() {
      this.getData()
  },
}
</script>
