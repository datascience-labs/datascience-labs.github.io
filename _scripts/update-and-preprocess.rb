# # go through projects and clean and update

# require 'yaml'

# $basedir = Dir.pwd						
# config = YAML.load_file("_config.yml")

# config["projects"].each do |repo|
# 	name = repo.split('/').drop(1).join('')		
# 	Dir.chdir($basedir + "/projects")			
# 	if !Dir.exists?(name)								# clone project repo
# 		`git clone https://github.com/#{repo}.git`
# 	end
# 	Dir.chdir($basedir + "/projects/" + name)			# drop into blotter dir	
# 	`git clean -f`										# remove untracked files, but keep directories
# 	`git reset --hard HEAD`								# bring back to head state
# 	`git pull origin main`								# git pull					
# end

# Dir.chdir($basedir)
# `ruby _scripts/preprocess-markdown.rb`
# `ruby _scripts/generate-project-data.rb`

require 'yaml'

$basedir = Dir.pwd
config = YAML.load_file("_config.yml")

config["projects"].each do |repo|
  name = repo.split('/').drop(1).join('')
  Dir.chdir($basedir + "/projects")
  if !Dir.exists?(name) 								# clone project repo
    `git clone https://github.com/#{repo}.git`
  end
  Dir.chdir($basedir + "/projects/" + name)				# drop into blotter dir	
  `git clean -f`										# remove untracked files, but keep directories
  `git reset --hard HEAD`								# bring back to head state
  branch = `git rev-parse --abbrev-ref HEAD`.strip		# get branch name
  if branch == 'master'									# git pull
    `git pull origin master`
  else
    `git pull origin main`
  end
end

Dir.chdir($basedir)
`ruby _scripts/preprocess-markdown.rb`
`ruby _scripts/generate-project-data.rb`