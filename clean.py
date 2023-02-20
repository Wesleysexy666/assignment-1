import pandas as pd

def clean(contact_info_file, other_info_file, output_file):
    contact_df = pd.read_csv(contact_info_file)
    other_df = pd.read_csv(other_info_file)
    merged_df = pd.merge(contact_df, other_df, left_on='respondent_id', right_on='id')
    merged_df.dropna(inplace=True)
    merged_df = merged_df[~merged_df['job'].str.contains('insurance|Insurance')]
    cleaned_df = merged_df[['respondent_id', 'name', 'address', 'phone', 'job', 'company', 'birthdate']]
    cleaned_df.to_csv(output_file, index=False)

    output_df = pd.read_csv(output_file)
    print(f"Output file shape: {output_df.shape}")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('contact', help='Contact info file (CSV)')
    parser.add_argument('other', help='Other info file (CSV)')
    parser.add_argument('output', help='Cleaned data file (CSV)')
    args = parser.parse_args()

    clean(args.contact, args.other, args.output)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('contact', help='Contact info file (CSV)')
    parser.add_argument('other', help='Other info file (CSV)')
    parser.add_argument('output', help='Cleaned data file (CSV)')
    args = parser.parse_args()

    clean(args.contact, args.other, args.output)

    # New code to commit the changes
    import subprocess
    subprocess.run(["git", "add", "respondent_cleaned.csv"])
    subprocess.run(["git", "commit", "-m", "cleaned data"])
