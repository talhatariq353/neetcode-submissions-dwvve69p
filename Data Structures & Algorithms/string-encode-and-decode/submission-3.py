class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "1#"
        else:
            string = []
            for i, word in enumerate(strs):
                string.append(word.encode().hex())
            return "##".join(string)



    def decode(self, s: str) -> List[str]:
        if s == "1#":
            return [] 
        else:
            words = s.split("##")
            for i, word in enumerate(words):
                words[i] = bytes.fromhex(word).decode()
            return words
