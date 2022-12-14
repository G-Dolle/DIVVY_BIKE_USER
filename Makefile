streamlit:
	-@streamlit run Hello.py

streamlit webapp:
	-@streamlit run pages/webapp.py

streamlit reco:
	-@streamlit run pages/reco.py

install_requirements:
	@pip install -r requirements.txt

install:
	@pip install . -U

clean:
	@rm -fr */__pycache__
	@rm -fr __init__.py
	@rm -fr build
	@rm -fr dist
	@rm -fr *.dist-info
	@rm -fr *.egg-info
	-@rm model.joblib
