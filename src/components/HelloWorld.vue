<template>
  <v-container fluid grid-list-md>
    <v-slide-y-transition mode="out-in">
      <v-layout row wrap align-center>
        <v-flex v-for="entry in entryList">
          <v-card>
            <v-card-title>
              <span class="headline">{{ entry.title }}</span>
            </v-card-title>
            <v-card-text>
              <blockquote>
                {{ entry.content }}
                <footer>
                  <small>
                    <em>&mdash;{{ entry.date }}</em>
                  </small>
                </footer>
              </blockquote>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-slide-y-transition>
  </v-container>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
import axios from 'axios'

export default {
  data () {
    return {
      entryList: []
    }
  },
  mounted: function () {
    console.log('mounted')
    axios.get('/api/entries/')
      .then((response) => {
        this.entryList = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
