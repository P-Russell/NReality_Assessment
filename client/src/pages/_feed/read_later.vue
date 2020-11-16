<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-12 text-center py-3">
        <h3 class="text-muted">{{ $route.params.feed }}'s Read Later List</h3>
      </div>
      <Feed read-later />
    </div>
  </div>
</template>

<script>
import Feed from '~/components/feed'

export default {
  name: 'ReadLater',
  layout: 'results',
  components: { Feed },
}
</script>
