SIG: Contributor Experience SIG
Date: 2026-10-05
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Amy Super** 00:21 Hey, Ernest.
**Ernest Owojori** 00:27 I hear me. Can you hear me?
**Amy Super** 00:30 How's it going?
**Ernest Owojori** 00:32 Going well.
Thanks.
Arba from your side.
**Amy Super** 00:37 Pretty good. I'm fighting off a cold, so my voice is a little hoarse, so, you know.
I'm glad that yeah. I'm glad you I'm glad you brought a topic to talk so that I don't have to do all the talking today.
**Ernest Owojori** 00:52 Oh my god. Yeah, that's okay.
Where are you based?
**Amy Super** 00:58 I'm in the US, in a city called Pittsburgh.
**Ernest Owojori** 01:02 Peter Parker, I have a friend here.
**Amy Super** 01:05 Do you?
**Ernest Owojori** 01:06 Yes, yes, he's in Cmu.
**Amy Super** 01:09 Oh, okay, got it. Yeah.
**Ernest Owojori** 01:10 Yeah.
**Amy Super** 01:13 Yeah, I'm… I grew up here, I'm from here. Hey, Dhruv.
**Ernest Owojori** 01:15 Oh, nice.
**Dhruv Ahuja** 01:17 Hello. Hey Ernest.
**Amy Super** 01:19 Yeah, yeah, and then I moved away a little bit, and then I came back, so, you know, I love it here. This is actually the best time of year here, because the temperature is perfect, and it's not raining. It's a really nice time to be here, so…
**Ernest Owojori** 01:33 Oh, great.
**Amy Super** 01:35 And where are you, Ernest?
**Ernest Owojori** 01:36 I'm currently in Lithuania.
**Amy Super** 01:39 Hmm.
**Ernest Owojori** 01:40 And to be precise, Venus, the capital.
**Amy Super** 01:44 Nice.
**Ernest Owojori** 01:45 Yeah.
**Amy Super** 01:47 So is it, 7:00 PM for you or is Lithuania one more hour later? Is it 8:00 PM?
**Ernest Owojori** 01:53 Yeah, 8pm, yeah.
**Amy Super** 01:55 Okay, yeah.
I lose track of where the line is, you know?
**Ernest Owojori** 01:59 Yeah, I actually go here not so long. I used to be in Nigeria.
So I'm still acclimatizing.
**Amy Super** 02:09 Yeah.
**Ernest Owojori** 02:09 Yeah.
**Amy Super** 02:11 Nice. Well, thanks for joining us today. I think we can probably just… oh, wait, Abhi's joining here, so we'll just maybe give it one more minute for other people to jump in, so… Hey, Abhi.
**Abhi** 02:23 Amy.
Happy Monday.
**Amy Super** 02:26 Yeah, same to you.
So I was just telling Ernest that my voice is a little messed up because I'm getting over a cold. So I'll try to not…
**Abhi** 02:35 be.
**Amy Super** 02:36 All the talking.
Yeah, right?
**Abhi** 02:39 Yeah, I've had a couple of colleagues who… At toddlers or kids going to school, bringing in.
COVID or pneumonia back home, and they're all on T days.
We're all looking off.
**Amy Super** 02:52 Yeah.
Yeah, I got COVID 3 weeks ago, and then I was better for, like, 4 or 5 days, and then I came down with this, and so I don't know if it's, like.
An extension.
**Abhi** 03:04 the.
**Amy Super** 03:04 Like, I don't know what it is, or if like maybe I was run down, so I got whatever other thing came along, but hopefully this is it, and I'm done because I have a lot of travel coming up, and I don't I don't want to be sad.
**Abhi** 03:16 better.
**Amy Super** 03:16 Thank you.
**Abhi** 03:17 Yeah, the.
The KubeCon is coming up next month, so.
It must be a business continuum.
**Amy Super** 03:26 Yeah, I have, Grafana Labs has a conference in two weeks.
**Abhi** 03:31 the.
**Amy Super** 03:32 Yeah, Observability Con. So I'll be there.
**Abhi** 03:35 And then.
**Amy Super** 03:36 I go to KubeCon, and then I have an offsite for the team that I work with. So.
**Abhi** 03:42 Okay.
**Amy Super** 03:43 lot.
**Abhi** 03:44 is.
**Amy Super** 03:44 you.
**Abhi** 03:44 So my previous team works a lot with Grafana and they got invited because usually Grafana Con, the Observability Con is in New York, so we were able to go, but this year is in San Francisco.
**Amy Super** 03:58 Yeah.
**Abhi** 03:59 No.
**Amy Super** 04:00 I honestly would prefer New York, because it's, like, a one-hour flight for me, but San Francisco is, like, a… almost, like, four and a half hour flight, so, you know.
**Abhi** 04:10 Where are you based out of?
**Amy Super** 04:12 I'm in Pittsburgh, so.
**Abhi** 04:13 Got it, sir.
**Amy Super** 04:14 I'm just I'm really like, yeah, I'm like 500 miles from New York, so.
**Abhi** 04:18 Yeah.
**Amy Super** 04:20 So.
Okay, I think we've given people enough time to join, so, if you all could just open the notes and put your name in as an attendee, that'd be awesome.
I just have two updates, and then maybe we can go around, and then Ernest is joining us today to share, the results of the post-merge survey, kind of, like, data collation.
So, definitely interested in that. So, but let's get the housekeeping out of the way. So just as a heads up, last week on… Wednesday, I appeared on What's New in OTEL. I dropped a link there if you all want to watch it. I never like watching myself, so I'm not gonna watch it. But, I would… one of the things that I was doing was.
encouraging more people to come join our SIG and talking about what we're working on.
So that's it for that one, and then the next one is.
Also, oh yeah, I didn't say this, this is at, KubeCon.
So at KubeCon, when I go, there's an Otel Contrib Fest, and this is, like, an area where Otel maintainers will hang out and help people to open and merge PRs in their particular repos. So I'm planning to go.
You know, and take a ton of notes and just listen and overhear, and try to hear what people are saying about what their experience is like as they're doing that. So hear from both the maintainers and the people who are working with them who came for help.
So, I'm pretty excited about that. That's gonna be a cool opportunity to do that in person. So… so hopefully I'll bring a lot of findings back and, some more ideas for ways we can make improvements So that's it for me. Anyone else have an update before we turn to Ernest?
**Abhi** 06:17 No, just if we're going to go around the room, right? Well, everybody's like, all right, cool. So nothing.
**Amy Super** 06:27 Wait, did you mean like Abhi, like I just went.
**Abhi** 06:30 I was just going to talk about that.
**Amy Super** 06:31 the.
**Abhi** 06:32 You know, I was just gonna get the update of what I'm working on.
**Amy Super** 06:35 Yeah, perfect. Go ahead.
**Abhi** 06:36 Yeah.
So, I had two other videos that I was gonna… Rakuta, I was on, like, two-ish weeks vacation, so got back. I have the PR, I was just opening the PR, actually, to share the script, similar to how I did it for the first one. It took a, like.
It was a learning experience for me as well, on how to record, how to edit, and then… look at myself talking and make sure that I don't… because I… similar to you, Amy, I was like, I don't want to watch myself again and again. It was, like, multiple takes, and then finally figured out how to do it. Fun experience now that I did it, like, 50 times to record that 5 minutes video.
But, I'm working on the other two. I know there's, one of them was for AI usage.
What somebody else was gonna be working on? Do we know if… they have started, or should we just finish the first screen, then reach out to them for the AI usage and projects?
**Amy Super** 07:42 Let me look, you know, I don't actually have our backlog open, so let me pop that open.
**Abhi** 07:48 Let me send it in the Zoom chat.
It was… AI usage. So it was issue number 98. Tyler was going to work.
**Amy Super** 08:00 Oh, yeah, Tyler. I talked to Tyler about this, and… Where we left it was that… He said… He has to rework the slides, so this is actually… he gave a short talk.
in the past, about this topic, and so he has, like, he has the content ready, but the slides are branded with his former employer, and so he wants to clean up the slides, so he's gonna do that before he records it, but he said that he would do it.
**Abhi** 08:38 Okay.
**Amy Super** 08:39 And that's… that's the update on that. So, so I would hold off on that one for now.
**Abhi** 08:45 Alright, sounds good, yeah, and I'll work on the others, which I have.
Currently in progress, and then, hopefully by then we can, we can go ahead and follow up with him.
**Amy Super** 08:55 Awesome, thank you.
**Abhi** 08:57 That was it for my son.
**Amy Super** 08:59 Okay.
Dhruv, how's it going? Anything else, anything new with you?
**Dhruv Ahuja** 09:04 Yeah, I just wanted to check on, whether you have gotten a chance to look at the previous set of questions for the survey.
You're muted.
**Amy Super** 09:20 Yeah, I haven't, because I was out sick, so, I will have a look at that.
**Dhruv Ahuja** 09:27 Cool. Yeah, so I think we ought to repeat a few questions, and I think beyond that, I had also just looked over it once. I haven't gotten the chance myself.
But I think we can repeat a lot of the same questions.
And then Andre was asking about the demographics, but I think that limiting it to just the continent itself makes sense to me, because people might not be comfortable sharing where exactly they live, maybe even the country itself.
So, I think even having, Continent level, like, awareness of where folks are coming from, where they are contributing from is fine, because it's mostly a remote endeavor, contributing to hotel.
**Amy Super** 10:14 So help me understand what is the question. So there's a question in there that asks like demographics, like where they're from.
**Dhruv Ahuja** 10:20 Yeah.
**Amy Super** 10:21 How specific was it in the old one?
**Dhruv Ahuja** 10:25 It was just asking, the continent, just a second.
Yeah, which region do you usually live in? North America, Central America, Caribbean, South America? Third option was EMEA, and the fourth was APAC.
So, I think we can go ahead with the same one, but if you feel we can be more specific, then I guess we can have an optional question asking people if they wish to reveal the country of their residence.
**Amy Super** 10:55 Yeah, I mean, I definitely would like to know by continent, because I know that there have been, like, time zone challenges in the past.
Especially for people in APAC with the earlier meetings. Like, trying to overlap with Europe is often difficult. So… You know, I do like your idea of, narrow, you know, optionally narrowing it down to country.
But I think what we should do is look and see how many questions we end up with.
Because if we have too many, I think narrowing it by country is one that we could drop.
And not lose a lot of content. So let's… let's keep that in mind, but not make it a hard plan right now.
Were there any questions that you felt like we should get rid of, or that don't make sense anymore?
**Dhruv Ahuja** 11:51 Let me just quickly go through it again.
I'm just looking at the PDF, because I noticed that the Google Doc that was linked to the GitHub issue, and the Google Form PDF that Pablo shared has some differences, it seems, or maybe just the order is different.
So I'm just looking at that PDF for time being.
I think maybe we should make this so there is a question about what what SIGs you have participated in the past year.
And then we have a big list of them. Maybe we can make it a free-form question, if that makes more sense. So people just type in the SIG that they go into.
Because I think the list is quite long.
**Amy Super** 12:46 Yeah, so.
**Dhruv Ahuja** 12:47 is not a concern visibly, then I think we can just use the same one and expand it to have the new SIGs as well.
Okay.
Yeah.
**Amy Super** 13:01 Okay.
**Dhruv Ahuja** 13:02 And I think, yeah, we should definitely keep the maintainer.
Question, because then that helps us further narrow it down, because I think one concern with the end-user survey as well was whether to include maintainers or not, because.
How much emphasis do we want to give to the maintainers when we are more concerned with the experience of the end users?
So, maybe that can also be one thing that we can consider.
So just having that question, and then filtering out the survey data, and then seeing whether we have enough data.
To have.
A good, enough set of answers and diversity.
Okay, I think.
**Amy Super** 13:44 sense.
**Dhruv Ahuja** 13:45 Overall, I think it looks good.
**Amy Super** 13:48 Okay.
Got it. Yeah, that all sounds good. I will put that on my to-do list to also take a spin through that.
And then, in terms of distributing it.
Is End User SIG going to do the distribution for us, or, like, do we need to do that? Do you know what that looks like?
**Dhruv Ahuja** 14:10 Yeah, I think mostly the end-user SIG would be advising us, and I think distribution typically happens via social media posts and sharing a blog post, so we can write a short blog post about it, and then ask the end-user SIG to share it.
On the socials, and then the… on the website, we can raise a PR.
**Amy Super** 14:32 Okay.
I did, on the What's New in OTEL, mention that we were going to be sending out a survey soon, so I at least gave everybody a hint that it's coming, so…
**Dhruv Ahuja** 14:42 Yep.
**Amy Super** 14:44 Cool.
Okay, yeah, that all sounds great.
**Dhruv Ahuja** 14:48 Yep.
**Ernest Owojori** 14:53 Yeah.
**Amy Super** 14:53 Is there anything… sorry, yeah, real quick, Dhruv, is there anything else you wanted to…
**Dhruv Ahuja** 14:58 No, no, my bad.
**Amy Super** 14:59 Okay. Okay. All good. Okay. Ernest, it's all you.
**Dhruv Ahuja** 15:02 I…
**Ernest Owojori** 15:03 Yeah, I agree.
**Dhruv Ahuja** 15:04 This part of just handing it over to the next person, my bad.
**Ernest Owojori** 15:08 Oh, it's okay.
Yeah, I think I will try to share my screen now.
Before I go to the presentation slide, I… Prepared?
I wanted to share context of what the data actually looks like.
So, based on what I understand.
The data has, like, theorem and something plus responses, but The insight has been shared with the SIG members before.
So, the, The ones that are recent are the ones that are collected within July and now, or June, within a few months, which is what I focused on. They were just about 60-something.
Responses?
And I… Went ahead and… I did some because the most important question here is what can we improve?
I did some open coding.
You know, just putting them into codes and trust me.
Those are not my… Forteo, how would I say that?
These are not things that I do on a normal day. I'm basically a quantitative person, but I'm beginning to appreciate the qualitative approach of analyzing things. So I was able to come up with some quotes, which I will go into details with the presentation.
Yeah.
Now, to what I found… Before I continue, please can you confirm we can… See my screen?
**Amy Super** 16:50 Yeah, we see the presentation.
**Ernest Owojori** 16:53 Can you still hear me?
**Abhi** 16:55 Yep.
**Ernest Owojori** 16:56 Good.
Yeah, so like I said earlier, we are like 64 responses across 8 repositories within July 13th to… October 2nd.
And within all the repositories, the collector country is like 53% of what people that responded to that form.
participating.
And followed by OpenTelemetry down the… down to the OpenTelemetry collector.
And, in terms of what their experience looks like on a very high level, people are actually Satisfied with what we currently have.
An average of 4.45 rating is very good in my opinion.
And 41 of 64 people actually gave a 5.
And only 2 rated below 3.
But, if we go into what people actually told us they needed us to improve.
When I categorized them and coded them into some categories and frequencies.
I found that like 40% of, you know, 40 people responded to that question.
And out of that, 16 of them, which is, like, 40%, actually said.
Our PR review time and responsiveness is not so great.
Then some people, many of them obviously said they are satisfied.
Why so long?
I also said documentation is a big problem because they don't actually know when to onboard. And I think this aligns with Ethereum.
Quality… qualitative study that Amy has done before.
Then there are some issues with CICD, but the list of… only just two people are complaining about easy sign-off, which I think my experience with that was not so, I won't say great, but.
It was not expected, I didn't often see that in other open source repositories, so If I have my real voice to say I don't want to sign a EZCLE sign-off.
Now, when I look into Among those, among the number of people that.
Among the issues that they want us to improve.
I actually find that most of it are largely concentrated on the colonial country.
Which makes sense, because when this survey is, devoted towards people that are exponent there.
And maybe… I wouldn't say that I won't say as a statement of fact that there are more contributors in Collect and Contrib.
But, for Java… There are just a few people, and those that actually responded were okay with their responses, because they said they were satisfied.
And, if I now go into the details of What people are actually saying. You could see some people say several reviewers were quick enough to review my PR, but it stayed blocked.
Because the requirement was not available.
For a minor documentation change, it was pretty time consuming.
This is… this is more of a governance issue, because, yeah.
And that happened in the Colento Contrib, and the person who returned was 305.
Another person said, reduce the time it takes for review. It was a simple change, and it took 4 each month from issue opening to PR being matched.
Another person said the same collector contribute.
The review process is not very transparent. You don't know when to expect your PR will be reviewed.
And uproot.
And some people, they say, as a new contributor, I was very confused because they had, like, 100 repositories under its organization. And it's all doubting to find a place to start.
So, another person said, they want us to make it clear who is the contact person for a particular change, and who needs to approve it.
Which is also a documentation problem.
Some people also say surface PR templates checklist at open time rather than mid-review. That is, some people don't have access to the PR template before they were done with the Issues that were assigned to them and in a way it breaks their hearts.
Someone also said they had issues, you know, seems to me that some build checks are not stable and huge error unrelated to MR at hand.
Someone said, you know, the mixed script, which I believe is in the CICD pipeline, didn't work out of the box on Mac.
you know, Docker socket mount points didn't match the Kolima.
And someone said the make file tool automatically generates changes to localization files which are not desired.
And later, have to be removed.
Some also complained about, the booth that we have.
Someone said when I was just waiting for a PR.
For your review on the PR, they both threatened to close my PR.
And I had to make a meaningless comment to prevent it from being closed.
I think I remember reading this review because the person said it was literally not him delaying the pull request and yet.
He was being threatened by the boat.
You know, someone else also said it would be nice if 1 of the many boats that responded to the PR told me what the next stage was.
Then, I think lastly, someone said it might be worth considering auto-formatting instead of having to manually fix mechanical issue. I think I also have a first-hand experience of this with.
Lint, you know, when you are trying to publish it.
A block, it takes a maintainer to actually Fix the formatting issue correctly.
Those are the way I could summarize it. You know, forgive me if this is not the best summaries you've seen for your qualitative study, but, you know, I think I enjoyed… coding the whole thing with myself and validating with the LLM that I'm using.
And I think, some of the insight that I found useful here is that we need to Dig into what happened.
in the OpenTelemetry collector country that people have to wait for a single person's approval for 4 months, because that's a serious governance problem.
That's my own opinion, I don't know what he thinks.
And I'm happy to hear Your thoughts.
**Amy Super** 23:30 Yeah, thanks for walking through all of this, Ernest. It's… this is all… I mean, I love data, so… I love this.
You know, in terms of what I think about, like, kind of review time.
I think this is actually, like, one of the most challenging topics for any open source community, right? Is that.
And this is just about time to review. And I think it's actually getting worse, because, I know a lot of the SIGs have… had a lot of AI-generated PRs just sort of, like, thrown at them full speed. And what that means is that the time to review is actually getting worse, because they're having to sort of sift through stuff that is, like, really verbose, but not high quality.
In order to, you know, determine if even if it's a good fit for, you know, the goals of the SIG.
So I… this is a really hard one.
I'm not surprised that, most of the responses came from Collector Contrib, because it's just, like, a really big… Like, there's a lot of people working on that, right? So, I would be kind of curious, Ernest, I don't know what your bandwidth is, but I would kind of love to see, not just… how many, responses there were, but, like, what the volume of PRs are for each of these repos. Because I think it would be interesting to see if it's, like, proportional, or if it's not. Do you know what I mean?
**Ernest Owojori** 25:13 you Like, like, the PRs that are currently open across each of these repos, right?
**Amy Super** 25:19 Yeah, or even… I'm trying to think of, like, maybe not what's open… I don't know, someone else jump in if you have an idea here, but, like, I'm thinking about, like.
You know, like, historically, like, average number of PRs.
Open per month or something like that. Just to get a sense of, like, volume, you know?
**Ernest Owojori** 25:38 Yeah, I can do that with the GitHub API.
Yeah. I think I can… I have a… I have a work in progress that I've been calling OpenTelemetry's repo.
It has not given results, I have not presented it, so I can easily do that, maybe tomorrow, and let you know if we… what the proportion looks like in terms of.
**Amy Super** 25:58 Sure, yeah, there's no… there's no rush on it, but I think it just would be interesting to see, because I think it's… it's hard to tell if, like, does that mean that Collector Contrib is problematic in how they're working, or does it just mean that, like.
they have a lot more traffic, right? So.
And then, I'm sorry, there was one more thing where at the end you said you were curious to hear our takes. Can you remind me what that was?
**Abhi** 26:25 My personal experience with Collector Contrib has been because they get so much of incoming data.
And, you're right, it's like, from what I've seen, in the PRs, it's just AI… Influx, has caused a lot of.
increased number of PRs, so it's definitely adding up to the… The reverse. I have had two lines of PR, which has been… left for review for last 3 months, so… I think everybody… I see multiple comments about the same issue.
Also, it's like, I don't know, it's probably around the world, like generally after October, things slow down. So it could be that as well. But I don't know when the survey was done.
**Ernest Owojori** 27:13 Yeah, the survey was, you know, I think he's an, he's an active surveyor whenever you.
They match your PR, the survey pops up.
And you decide to do it or not. So for this particular study, it was responses within July 13th to August 2nd.
Sorry to October second.
**Abhi** 27:35 Okay.
Yes, sir. Yeah. Collector contract, yeah, I mean, definitely, that's a lot of PRs, because that's… which has the most number of, good first issues, and… People, go ahead and just… use AI to create a PR and then just, keep hammering the reverse down with those.
**Dhruv Ahuja** 27:53 Yeah, I've personally seen a few of, like… and this is a big thing in Indian colleges, especially, like, I had a couple of my cousins come up and say that, okay, I've got this ChatGPT plan, and I'm just asking it to crawl the internet to find me good first issues that I can just Contribute to and then they're not even doing that, they are just running the GPT or Astro or whatever the latest model is to do the whole thing for them, so it's terrible.
Especially with the big repository. So, and they have filters, like, it must have 10,000 stars or above. They are, like, investing all this time into this thing, rather than actually learning the fundamentals of open source.
And, yeah, on the reviews, we note I've seen it, for other smaller repositories as well, where the maintainers are just… have their hands full with other tasks or their day job, so…
**Ernest Owojori** 28:51 Yeah, I think we… we need to… I will have to… I am curious to the problem that I had from you guys today.
Because, this is the kind of research that I do for my research space, and I think I want to read what people are thinking about that in the general open source space, to know what are people doing, what are we going to solve this problem, really?
Because, we are not going to stop people from using AI, are we?
**Amy Super** 29:22 No, we're not going to stop.
**Ernest Owojori** 29:23 people.
**Amy Super** 29:24 from using AI, and actually, there have been a couple of places where… and this is something that I think I want to add to our backlog. I'm sorry, I just put a cough drop in, so if I sound weird.
But, I'm not sure that our… so our current guidance on AI, like, we've kind of put together some, like, templates for how maintainers can respond if something looks, like, sloppy, and some of the SIGs have put, kind of, like, guidelines in place.
But what I'm not sure is if we've actually documented this.
in any of our, like, contribution materials. And so, I'd like to put an item on our backlog to, like, review our contribution materials and make sure that any guidance that we do have is easy to find and available.
Because I'm not sure that it is right now, but I know that I've seen, like, stuff kind of, like, flying past of, like, oh, here's an… here's a response that I used, maybe you'll find it helpful. And then so… and it's, like, in Slack, but I don't know that it's actually hitting our actual docs.
Have any of the rest of you seen this in our contribution materials?
**Abhi** 30:44 There is an AI usage doc on the main page.
Also, like when I was creating the introduction video, there is like, I did include the AI section.
A lot of repos are adding it, and also our… main, like, the landing page on OpenSimulator.com has some details on, like, what our expectations are on using AI, and how, there are, like, agents at MD in each and every most of the repos to, filter out, like, or to make sure that people do not just, check in or, create PRs with Slop.
So there, there are places which has those.
But I think we could make it more obvious, given that increase in AI usage. It would be helpful to have that more evident and in more places that people look at it first.
as Dhruv mentioned, it's not even people looking, it's AI looking, so we can do something to… to make sure that, AI, does not include these, or, like, we could… we could give instructions that, hey, to not create PRs on, And repos with certain limitations and sections.
**Ernest Owojori** 32:07 Yeah.
While I think, it is very difficult to get people To actually contribute, gain of value.
I also think… We might not… I don't… well, it is my opinion. I also think, There is a deviation in… How fast it takes now to develop anything I want to do compared to how fast it can take to review them.
Which, directly or indirectly, will affect our time to match.
I mean, time to merge EPR.
Even if people try to be honest, which we cannot control.
And actually contribute what they know.
They will do it faster.
Right? Now… How are we going to are we going to say we are able to also review it as fast as they can build it?
I don't think so.
I'm just talking generally now as a product.
**Amy Super** 33:07 this.
**Ernest Owojori** 33:07 space.
**Amy Super** 33:08 Yeah, I don't think that we'll ever be in a position where reviews are as fast as creation when creation is done with AI.
Like, I just don't think that that's realistic.
And I've seen… you know, like, I've seen different ways of doing this, and this is, you know, outside of OpenTelemetry as well. I've seen some… things where, like, your PR description needs to be human-written.
Right, because you need to be able to actually say, like, this is what I changed, and I understand what I changed, and if you can't write that description, then you don't get to… you should not be submitting that PR, right? That's something that I've seen, that's… that's being tried somewhere else.
You know, I think there are… that's one idea. There are a few other ideas that… You know, with comments and stuff.
too, that, like… and this is something that I think maybe could also go into some of the guidance, is that, like.
A lot of people, from what I have heard.
One of the things that people like to use AI for is, especially if English isn't their first language.
And I think that's completely understandable, but at the same time.
as a native English speaker, I would rather read somebody's, like, not perfect English than read Claude every day, all day long, right? You know? I'm more than happy to, you know… and so… but I think that that's hard to… overcome if you're feeling uncertain of yourself, right? And you want that crutch of having Claude rate it correctly for you. So, it's a… yeah, it's just, like, a really tricky subject, I don't know. I don't know that we have any answers.
**Abhi** 34:55 I prefer making spelling mistakes these days, because just to be sure that it's not written by AI.
**Amy Super** 35:03 Yeah, that's how you tell that it was a person, because there's a wait.
**Ernest Owojori** 35:06 Every day.
**Amy Super** 35:07 The AI is going to start introducing typos because it's going to think that we want to see typos, right? You know?
**Abhi** 35:13 Yeah, yeah, it's not… it's not too far out, I'm sure.
**Ernest Owojori** 35:18 Yeah, you know, honestly, if I tell my Claude.
To make it human by making a few random typos, it will do it.
So, yeah.
**Amy Super** 35:30 Yeah, it was.
**Ernest Owojori** 35:30 Randy.
**Amy Super** 35:31 would.
**Ernest Owojori** 35:32 We are in a very serious problem where what we have seen to help us is creating quite a great deal of problem for us.
Yeah, it is what it is.
**Dhruv Ahuja** 35:43 Might be worth asking the maintainers who have implemented a limit on the number of PRs that a person can open. I believe if they're not a member, the rule is something like that, which GitHub added recently, whether they are seeing any positive effects of that or not.
**Ernest Owojori** 36:00 Yeah, I think I saw something on Airbiz, I think you know Airbiz, this, Where people publish their pre-print and all.
They… last month, they reduced the number of papers that people can submit to 2 within a month.
**Dhruv Ahuja** 36:20 Yeah, I think we, there was a discussion similar to that in hotel maintainers as well, where people have started asking for limits, or I believe the repo owners can now start setting limits.
On a per repo level, so it might be worth investigating that, whether that is having a positive impact for them or not, because I think it's been a few weeks since I read that conversation.
**Ernest Owojori** 36:44 Where? Do you remember the SIG?
**Dhruv Ahuja** 36:47 Hotel maintenance channel.
**Ernest Owojori** 36:49 Okay, what time it is.
**Dhruv Ahuja** 36:51 But I think you'll have to do a Slack search to find… What about…
**Ernest Owojori** 36:56 Yes, yes.
Yeah, we could… I don't know how long they've been doing that.
We could try to assess how impactful it is. If it reduces it, maybe we can recommend it across the audio repositories.
Because, yeah, that was one thing I read that Evis did. I don't know if I'm even pronouncing it very well. Just happened.
Yeah.
I will find out, thank you for letting me know Dhruv.
I think I can stop sharing my screen.
**Amy Super** 37:30 All right.
**Ernest Owojori** 37:31 Oh, yeah.
Yeah, the.
And I was going to say that I think Did I stop already?
**Amy Super** 37:42 You stopped. You're good.
**Ernest Owojori** 37:43 Okay, I'm going to, I think I will begin to join the SIG.
More for now, but maybe the line of my work might be different from what everyone is doing.
I am interested in finding out.
Issues with data, qualitatively or quantitatively, because that's my research interest.
Yeah, so… Very cool.
**Amy Super** 38:05 Well, Ernest, we'd be happy to have any help you want to, you know, pitch in on, you know, this type of.
information is super interesting and helpful, so, you know, you're always welcome to join. I will say that, like, of the SIGs, this is probably one that is a little small, and so, you know, things might… and, you know, people have travel, or they're sick, or they're on vacation, or whatever, they're busy, they're… job, so sometimes things take a little while, but we try to, you know, plug away at it and make improvements where we can, so…
**Ernest Owojori** 38:40 Yeah, thank you. I think I would have added it to my calendar now. That's why I remember the easy meeting.
**Amy Super** 38:45 Awesome.
**Ernest Owojori** 38:47 On the issue, it was recommended that we write a blog post, but in my own opinion, I don't think I should be writing a blog post for this.
For this work, I don't I don't want to.
There's already a lot of backlogs. I don't think I should.
So, if you agree with that, I can just let Andre know that. Let's wrap up the blog post.
**Amy Super** 39:06 Yeah, I think that's good. You know, I think this is really helpful data for us. I don't know how… much people who are reading the OTEL blog want to get into the details on this type of, like, ongoing… it's almost like, infrastructure of an open source project, right?
**Ernest Owojori** 39:25 Yes.
**Amy Super** 39:25 So, yeah, I mean, I if you need us to say, like, yeah, you're good for you know, to tell Andre, then I'm fine with that. So and if not, I can take it up with him because I know him pretty well. So.
**Ernest Owojori** 39:36 No. Andrew was my mentor while I was doing LFX. Oh, nice. Yeah. He was the one that even shared the AJ with me. I didn't know about it.
**Amy Super** 39:47 Good.
**Ernest Owojori** 39:48 Yeah.
**Amy Super** 39:49 Yeah.
**Ernest Owojori** 39:49 Sounds good.
**Amy Super** 39:51 Okay.
**Dhruv Ahuja** 39:52 So.
**Amy Super** 39:53 This has been great.
**Dhruv Ahuja** 39:54 Yeah, you'd be sharing that in the maintainer's channel or somewhere, right?
For everyone else to see.
**Ernest Owojori** 40:02 Yes, I will.
**Dhruv Ahuja** 40:04 Cool.
**Ernest Owojori** 40:05 Let me try and join the channel now.
**Amy Super** 40:11 Yeah, Ernest, if you want an example of what it might look like to share out… so one thing I might recommend is, when I share out my research, I do tend to record a little video.
And it doesn't have to be perfect. It's not like the kinds of videos we're posting on YouTube.
where we're editing ourselves, right, Abhi? But, I do like to do a little walkthrough, because some people do consume content better as video than by reading.
So what I usually do is just record a little video of exactly what you just did for us here.
And then I just share it on Slack. Here's a video, here are the slides, and maybe here are, like, the top 3 findings, right? And if you would like, I can link you to one where I shared out our, qualitative research. If you'd like to use that as a template, you're more than welcome to.
**Ernest Owojori** 41:02 Yeah, I think I have the slide of the research, the newcomer one, right?
But I don't… I don't have the video.
Yeah, he's a newcomer, excited AD.
**Amy Super** 41:12 Yeah, I will find that for you.
But I will not do it while we talk. I'll just ping you on Slack with it, because if I do it while I talk, I can't talk and type at the same time. Yeah.
**Ernest Owojori** 41:30 It's okay, it's okay. No rush.
Thank you.
From my end, that's all, you know. Thank you for… Okay.
**Amy Super** 41:50 Cool. Well, thanks so much for that, Ernest. It was really, really helpful.
I think that's it for the agenda today. Does anyone else have anything they want to share or bring up?
Nope. Alright, cool. Well, thank you all for your time, and Ernest, I'll ping you a link to that Slack message.
**Abhi** 42:14 Good one.
**Dhruv Ahuja** 42:15 Thank you.
**Amy Super** 42:16 Have a good day, everyone. Bye-bye.
**Ernest Owojori** 42:18 Yeah, right.
