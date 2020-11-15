import { API } from '../plugins/api'

const api = new API()

export const state = () => ({
  entries: '__LOADING__',
  filter: null,
})

export const mutations = {
  setEntries(state, entries) {
    state.entries = entries
  },
  removeEntry(state, entryId) {
    console.log('alling remove entry')
    state.entries = state.entries.filter((entry) => entry.id !== entryId)
  },
}

export const getters = {
  entries: (state) => {
    return state.entries
  },
}

export const actions = {
  async fetchEntries({ commit }, data) {
    commit('setEntries', '__LOADING__')
    const entries = await api.fetchFeed(data.handle, data.readLater)
    commit('setEntries', entries)
  },
  async setReadLater({ commit }, data) {
    console.log('Calling set read later store')
    await api.addToReadLater(data.handle, data.entryId)
    console.log('After api call')
    commit('removeEntry', data.entryId)
  },
}
