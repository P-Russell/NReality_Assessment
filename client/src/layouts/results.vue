<template>
  <div>
    <NavBar />
    <Nuxt />
  </div>
</template>

<script>
import NavBar from '~/components/navbar'
export default {
  name: 'ResultsLayout',
  components: { NavBar },
}
</script>
