from Bio import Entrez
import multiprocess as mp
# the next two lines are needed to create an environment in which the 
# ssl doesn't complain about non-existing public keys...
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class GetReferences:
    def __init__(self, email, api_key, id):
        self.email = email
        self.api_key = api_key
        self.id = id


    def load_file(self):
        Entrez.email = self.email
        file = Entrez.elink(dbfrom="pubmed",
                    db="pmc",
                    LinkName="pubmed_pmc_refs",
                    id=self.id,
                    api_key=self.api_key)
        results = Entrez.read(file)
        return results


    def get_references(self, results, amount_of_references=10):
        references = [f'{link["Id"]}' for link in results[0]["LinkSetDb"][0]["Link"]]
        
        return references[:amount_of_references]

    def retrieve_records(self, references):

        xml_references = [f"{references}.xml"]
        print(xml_references)
        for reference in xml_references:
            text = Entrez.efetch(db="pubmed",
            id = reference,
            retmode="xml",
            api_key = self.api_key)

            f = open(reference, "w")

            f.write(text.read().decode("utf-8") )
        
    def multiprocess(self, refereces):
        with mp.Pool() as p:
            res = p.map(self.retrieve_records, refereces)

test = GetReferences("mk.wierenga@st.hanze.nl", "88e4e31fd21ef106e35256ae00d9626b8208", "30049270")
file = test.load_file()
references = test.get_references(file)

test.multiprocess(references)
