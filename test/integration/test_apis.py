""""""

from lib.services.apis import NCBI, ClinicalTrials, Medline
from settings import NCBI_API_KEY, logger


def test_medline():
    medline = Medline(logger)
    medline_data = medline.fetch_medline(icd10_code='J45.40')

    assert medline_data is not None
    assert isinstance(medline_data, dict)
    assert 'feed' in medline_data

    feed = medline_data['feed']

    assert {'id', 'author', 'subtitle', 'category', 'entry'}.issubset(feed.keys())

    entry = feed['entry']

    assert len(entry) > 0

    assert 'asthma' in entry[0]['title']['_value'].lower()

def test_clinical_trials():
    clinical_trials = ClinicalTrials(logger)
    clinical_trials_data = clinical_trials.fetch_clinical_trials(query='asthma')

    assert clinical_trials_data is not None
    assert isinstance(clinical_trials_data, dict)
    assert 'studies' in clinical_trials_data

    studies = clinical_trials_data['studies']

    assert isinstance(studies, list)
    assert len(studies) > 0

    study_1 = studies[0] if studies else None

    assert {'protocolSection', 'derivedSection', 'hasResults'}.issubset(study_1.keys())

def test_ncbi():
    ncbi = NCBI('my@email.com', logger, api_key=NCBI_API_KEY)

    ncbi_data = ncbi.fetch_ncbi_studies('asthma')

    print(f"NCBI data: {len(ncbi_data)}")

    assert ncbi is not None
    assert isinstance(ncbi, NCBI)
    assert ncbi.api_key == NCBI_API_KEY
    assert ncbi.logger is not None


def main():
    test_medline()
    test_clinical_trials()
    test_ncbi()
    print("All tests passed!")

if __name__ == "__main__":
    main()
    print("Tests completed successfully.")
