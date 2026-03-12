SIG: End-User SIG
Date: 2025-09-11
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Victoria Nduka 00:03:58 Hi, Enes.
Good evening.
Ernest Owojori 00:04:05 Victoria, good evening. Hope you had a good day.
Victoria Nduka 00:04:13 My day was boring, we'll see.
Ernest Owojori 00:04:18 I guess it's one of those days.
Victoria Nduka 00:04:25 Yeah, I guess so.
Ernest Owojori 00:04:30 Are you currently a… How was your dean?
The early part of my day was more of recovering from yesterday's work, but from afternoon, I think I enjoy it.
Every bit of it, still.
Victoria Nduka 00:04:50 That's nice. Hopefully.
Ernest Owojori 00:04:51 Yeah, yeah.
Victoria Nduka 00:04:54 Hi, Andre.
Andrej Kiripolsky (Grafana Labs) 00:04:55 Hello, folks.
Ernest Owojori 00:04:57 Hi, Andre, good.
Good evening.
Andrej Kiripolsky (Grafana Labs) 00:05:00 Yeah, good evening to you as well. How are you?
Ernest Owojori 00:05:05 I'm fine.
Andrej Kiripolsky (Grafana Labs) 00:05:07 That's good, that's good, that's good.
Ernest Owojori 00:05:10 Hope it's okay to just keep my video off.
Andrej Kiripolsky (Grafana Labs) 00:05:12 Sure, sure, whatever works for you.
Ernest Owojori 00:05:15 Thank you.
Andrej Kiripolsky (Grafana Labs) 00:05:16 Yeah. Victoria, we haven't talked for a while. How are you?
Victoria Nduka 00:05:20 Yeah.
I don't know, I don't feel… I don't feel too well.
Andrej Kiripolsky (Grafana Labs) 00:05:25 Oh. I'm having…
Victoria Nduka 00:05:26 Headache.
Andrej Kiripolsky (Grafana Labs) 00:05:28 Oh, that sucks.
Victoria Nduka 00:05:29 10% headaches exist since yesterday.
I don't know why.
Andrej Kiripolsky (Grafana Labs) 00:05:35 Yeah. Hope you feel better soon.
Victoria Nduka 00:05:38 Yeah.
I try, I try to sleep.
Well, sequel.
That nights.
Yeah.
Andrej Kiripolsky (Grafana Labs) 00:05:48 Hi, Dan.
Dan Gomez Blanco 00:05:49 How's it going?
Victoria Nduka 00:05:50 Hi, Dan.
Ernest Owojori 00:05:53 Bye, goodbye.
Andrej Kiripolsky (Grafana Labs) 00:05:55 Pretty good. How are you?
Dan Gomez Blanco 00:05:57 Good, good.
I think we've got a new joiner today, right, Ernest?
The dog just… The doctors went mental with that.
diaries.
Reese Lee 00:06:27 That light is… Well…
Victoria Nduka 00:06:30 Nope.
Hi, Reese.
Reese Lee 00:06:35 Hello, Victoria!
Hey, Andre.
Lisa?
Andrej Kiripolsky (Grafana Labs) 00:06:53 I just want to say sorry for that barking, my dog always gets totally crazy when somebody rings the doorbell, so there's not much I can do about it.
Dan Gomez Blanco 00:07:05 It could…
Reese Lee 00:07:06 Underdog.
My dog is… Yeah, I don't… I don't think we could really hear it.
Lisa Jung 00:07:14 Yeah, this is Ellie! Say hi, Ellie!
Victoria Nduka 00:07:18 She has no idea what's going on.
Lisa Jung 00:07:29 I can't believe summer's over. It's like September. What the heck, what happened?
Reese Lee 00:07:36 I know, I know!
Dan Gomez Blanco 00:07:41 I was talking to someone the other day, and I was like, I can't believe that 2025 is not lasting longer than a year. I think it's been, like, you know, like, 2 years. I've been in 2025.
Lisa Jung 00:07:49 For two years already, I think.
Reese Lee 00:07:55 It feels simultaneously… simultaneously like it's been really long, and really fast.
Dan Gomez Blanco 00:08:02 Yeah, yeah.
Lisa Jung 00:08:03 Totally.
Dan Gomez Blanco 00:08:06 Lots of things happening in Hotel, too, as well.
Reese Lee 00:08:09 Oh, yeah.
Dan Gomez Blanco 00:08:11 Oh, yeah.
Reese Lee 00:08:12 I'm like… So behind that stuff.
Andrej Kiripolsky (Grafana Labs) 00:08:28 Alrighty, shall we get started, maybe? We're already almost 5 minutes in.
Oh, jeez.
Dan Gomez Blanco 00:08:34 Cheers.
Andrej Kiripolsky (Grafana Labs) 00:08:35 Yeah, so I have the first agenda item, and that is, that I would like to introduce you, Ernest, our mentee for the LFX mentorship.
Reese Lee 00:08:50 Hello!
Andrej Kiripolsky (Grafana Labs) 00:08:51 We're running with Adriana, and yeah, Ernest will be working with us for the next 3 months, helping us, figure out the survey analysis.
things, like, everything related to survey analysis, and also communication of survey findings. So, yeah, welcome, Ernest. We are very happy to have you, and yeah, if you want to say some words about yourself, you are… you would be very… Very welcome.
Ernest Owojori 00:09:19 Oh, thank you so much, Andre, and it is my pleasure to meet everyone.
Like Andrew said, I'm honest. I like to see myself as a… data and polar professional, because I started my career as a data scientist.
Lisa Jung 00:09:35 Do I have a statistics background for my bachelor's?
Ernest Owojori 00:09:38 Then I started trying to intercept everything I do with Broadrot, and… lo and behold, I am sort of interested in understanding how people approach communities, online communities, from the research perspective.
Which means I use computational… qualitative models or tools to try to answer changes in human behavior on social communities, in which open source community is one of them. And I'm happy to be joining, the open telemetries group, particularly the end users group.
to refine how we analyze surveys and communicate insights. Thank you.
Reese Lee 00:10:15 Oh, awesome! Well, welcome!
We're terribly excited.
Ernest Owojori 00:10:20 Excellent.
Dan Gomez Blanco 00:10:21 You're welcome. Yep. And yeah, really looking forward to working with you as well.
Ernest Owojori 00:10:26 Yeah, same here.
Andrej Kiripolsky (Grafana Labs) 00:10:28 Yeah. So yeah, if you want to check some details about the project, I shared the project link, but I've shared it also before, so nothing new there.
And, yeah, I think next point is from Adriana, but I think… well, she mentioned to us that she.
Dan Gomez Blanco 00:10:44 might join later.
Andrej Kiripolsky (Grafana Labs) 00:10:46 I can… like, unless somebody knows more about it, then I can read it and just tell you what…
Dan Gomez Blanco 00:10:54 Should we go through the other ones first, just in case Adriana's able to join?
Andrej Kiripolsky (Grafana Labs) 00:10:59 That's a good idea, that's a good idea.
So, then I will continue with the next one, and that is end the user page on Opentelemetry.io. So, if you remember, there was this issue… about, like, where we were discussing that some updates to the page would be good. And, after a really long time, I eventually picked it up, and I came up with quite a big Quite big changes to the page.
not only related to the stuff that is in the issue, but it's also about making the page and the subpages a little bit structured in a bit different way, and getting rid of some of the subpages. So, yeah, I have a proposal ready. I'd like to ask you folks to take a look.
Let me know what you think. And… yeah, I'm aware that it might be a little bit of a… like, too big of a step at one time, so perhaps, yeah.
If… if the changes will be too big, I am happy to just tweak, like, yeah, break it down into… into more, smaller, smaller changes.
Yeah, thanks for sharing.
Dan Gomez Blanco 00:12:19 Yeah.
Reese Lee 00:12:20 Thank you for putting this together.
Dan Gomez Blanco 00:12:22 Yeah, that's awesome.
Reese Lee 00:12:23 Yeah, already this is looking… Much more organized.
Andrej Kiripolsky (Grafana Labs) 00:12:29 Yeah, yeah, that was, that was the goal, like, the original issue was more about, like, add some smaller things to the page, but it felt a little, like, not that structured, so I thought I would just, like, structure it a little bit better. Also, I wanted to surface all the… information related to end users, or relevant to end users, on the main page, and leave more of deep dives, and just, like, contribute to relevant information on the subpages. And also, I made the list of subpages shorter, because originally there were, like, 7 of them.
One was deprecated.
one, I was able to take the information and move it up a little bit, so… yeah, and… Oh…
Dan Gomez Blanco 00:13:20 Yeah, I also think that the interviews and hotel in practice.
Andrej Kiripolsky (Grafana Labs) 00:13:25 could be merged together, but it's perhaps something for… for a separate work. But yeah, that's… that's it, so… Yeah, please take a look, and I'm very much looking forward to any feedback. And actually, I didn't share the PR, so let me share the PR.
Dan Gomez Blanco 00:13:42 Could you, yeah, just for the PR, could you mark it as… Ready for review. I think it's still in draft, so we can get… otherwise, you know, it won't get reviewed by the comms, say, either.
Andrej Kiripolsky (Grafana Labs) 00:13:53 Oh yeah, sure, sure, sure.
Dan Gomez Blanco 00:13:57 But yeah, that's… I think I had a brief look before, it looks… looks great. But yeah, I think, I'll add some comments whenever I can.
Andrej Kiripolsky (Grafana Labs) 00:14:06 Thank you.
Alrighty, and if there are no comments now, then you can go ahead with your next point.
Dan Gomez Blanco 00:14:21 There's one thing that I saw there on your PR, which is the… Yeah, I think it's… when you pull the changes from the… from OpenTelemetry.io into your fork, sometimes, you know, there's a fixed all… command, npm run fix all, I think that, I think what you see in there, if you go to Files Changed…
Andrej Kiripolsky (Grafana Labs) 00:14:43 Yes.
Dan Gomez Blanco 00:14:45 let's see… yeah, so those were in the, you know, the submodule ones, I think, that may…
Andrej Kiripolsky (Grafana Labs) 00:14:54 Yeah.
Dan Gomez Blanco 00:14:54 I think that basically… I think if you run npm run fixhole, that should… Pull the… the dependencies, or pull the SAT modules and update it. I think something weird is happening here, I've seen that before. But, yeah, give it a go with PM, because you haven't touched these, right? So…
Andrej Kiripolsky (Grafana Labs) 00:15:13 I don't know, and I already did this before, that I unintentionally committed these.
module changes. I wasn't… I didn't know how to fix it, so I actually opened a separate PR, but yeah, now I will try to do it the proper way, and yeah, I'll try to fix all.
Dan Gomez Blanco 00:15:30 Yeah, so that, that, do that NPM run fix-all, I think, might help.
But yeah, that's cool.
Alright, I've got 3 things, that I wanted to… chat about, see if, Adriana… Joins in the meantime.
First one is the, the… this issue in the… in community groups. So, anyone that's ever signed up to a community group event, it's not the nicest experience, because you click on RSVP, And then it asks you to input your… Name, email, which… you already should have already, because you've already part of… you know, you need to register to… to the tool to be able to cite to RSVP. But then, company name, and blah blah blah, so I think, you know, what we try is to remove that, but you cannot Remove the pre-workshop survey.
on the community groups, on the CNCF Community Groups website. So what they've proposed is that we move them The… the, the OpenTelemetry community group to a virtual group, which makes sense.
There was a question if we wanted to call it OpenTelemetry Online.
I think, adriana Reese and I didn't really like that.
OpenTelemetry Online thing, but OpenTelemetry Live… It's, it's something that could work.
I guess there is a potential thing of calling something OpenTelemetry If it's a virtual team, right? If it's a virtual group. So anyway, so I tried, now that it's been moved to a virtual group, but I can still see that I cannot change the… that pre… Pretty, pre-event.
Survey?
or pre-order survey, that's what it's called. So let's see if they respond. But yeah, just to let you know that if we were to create a new event on the CNCF Community Groups, you'll still… yeah, in this one here, you'll still… Mmm… need to input some data that I don't think anyone wants to input, and I think it's probably damaging, or has VP numbers, to be honest.
Because a lot of people would be like.
you know, I don't want to… I don't want to give you my… My city of residence, or whatever.
Reese Lee 00:17:59 Yeah…
Dan Gomez Blanco 00:18:01 I forgot what it was, but if you… yeah. I don't… we don't have any event live right now, but… But let's see if we can… we can sort that out.
Moses, it really bothers me, and I mentioned that there. If you go to the… here, they already removed the fact that, for some reason, OpenTelemetry was in… you know, OpenTelemetry CA, based in San Jose, California. No, it's not. Or maybe San Francisco. But if you go to the main page, to the Cloud Native Community Groups, if you click on that… And if you scroll to the bottom, you'll see… and if you go here to virtual, in the top thing.
Reese Lee 00:18:40 Ritual, ritual.
Dan Gomez Blanco 00:18:41 We're still basically listed as, like, OpenTelemetry California.
As someone from Scotland, I'm not…
Reese Lee 00:18:51 Yeah, that's confusing.
Dan Gomez Blanco 00:18:52 It's weird, so I, you know, I just try to fix these, like, small things, right? But.
Reese Lee 00:18:58 Blind and visually impaired in Nebraska. Okay.
Neodiversity Pennsylvania, that's funny.
Dan Gomez Blanco 00:19:07 I think if they're virtual, they shouldn't have a, you know, Allocation, right, as the point.
Anyway, so that's one thing. The other one, let me see if I can link it here as well, is that the OpenTelemetry, in case you're… this is gonna be something that we'll probably be announcing… more widely at some point soon. Just wanted to give a heads up here, because I think it's useful as well for end users.
is the OpenTelemetry roadmap. So, One second, let me just find the link. See what I mean?
problem, if I can't find the link right.
Reese Lee 00:19:47 Mmm… Can we… is it to the point where we can, like, Google it?
Dan Gomez Blanco 00:19:54 Not yet, it's not been linked in the website, and there is a repo.
But the most important thing is This, let me just add it to the notes.
Right.
So that link.
Reese Lee 00:20:14 Yep, let me turn.
Dan Gomez Blanco 00:20:17 So, this is taking, at the moment, the projects, that are being driven across OpenTelemetry with some I would call it open source target dates, so… Because target days are a lot more difficult in open source than in a… than in a company, right? But yeah, so this should give people an idea of, like, you know, what is OpenTelemity working on? What is, you know, each of their deliverables. If you click on any of them.
Play that one.
Hmm.
I shouldn't be… Me opening that ticket, maybe it is.
Tuv, if you click on that one.
Yep, on any of them, basically. If you click on the… then that basically links you to, one, the README, but also, it links you to the… Project board for it.
And then you can link to the project board directly from the issue, so that's the title, and…
Reese Lee 00:21:23 Huh?
Dan Gomez Blanco 00:21:24 So if you go back to the… to the issue.
See the… what it says, yeah, so that… the quality of configuration stability.
Yeah, so that… Stakes directly there, right.
Yeah, so the idea here is that end users sure have an easier way.
of seeing what's happening across OpenTelemetry, what can they help with, what is, you know, if things that are here, for example, if you're interested in, hey, come and help us stabilize the declarative configuration, all these other things.
Not in the backlog.
So yeah, that should… That should help.
That's what we're aiming for, is for this to also contain Not projects.
that are OpenTelemetry… across OpenTelemetry, but also individual things that a SIG may be working in… may be working on.
And… like, I don't know, if you wanted to do, like, something that is worth mentioning in the OpenTelemetry roadmap, like… I don't know, the JavaSig is… stabilizing… or Python, for example, working on stabilizing logs. That is not something that is an OpenTelemetry-approved, like, project with, with GC approval. It's, like, something that a specific SIG are doing. The idea is that that will help drive, that as well.
So they… so a specific set.
And go and say, I want this to be in the hotel roadmap. And I've got a project board.
that's in the hotel, and I want, you know, and that project board basically gives me the deliverables that I will… be working towards.
So, yeah, those are the SIGs on the left.
Reese Lee 00:23:08 Got you. So, is the…
Dan Gomez Blanco 00:23:14 It's one of the goals for all the SIGs to have.
Reese Lee 00:23:17 Something on here, or just… Nice.
Dan Gomez Blanco 00:23:20 they don't need to… there's not… there's no requirement in a SIG to… for every SIG to have something here, but I would expect that we'll see more of that as SIGs move towards, like, having their main priorities.
Something that is… you know, FSIG is operating and, like, you know, just… Doing, like, bug fixes and small things. Well, that, you know, that doesn't really require That doesn't… that's not something that we would announce in a roadmap session, right, and say, hey, you know.
we're delivering… Something that is… or we're working on something that… It's a big project.
Then that will be… that will be in there.
Reese Lee 00:24:04 Bang.
Cheers.
Dan Gomez Blanco 00:24:06 All this is synced automatically from… so these are issued.
Synced automatically from… the projects themselves.
Reese Lee 00:24:16 Cool, okay.
Dan Gomez Blanco 00:24:18 So if you open, for example, I don't know, anyone that has a date on it, the auto arrow one, yep.
And you open the project, see how it says on track in the top right?
And then, if you click on that.
You will see the latest status update, which in this case.
Lisa Jung 00:24:36 Hmm.
Dan Gomez Blanco 00:24:37 Go to my meat, but, like, the idea is that, you know, project leads will be… Given their updates. Say, okay, we're still on track to deliver this by this date, and then… Yeah, that gives… what we're trying to do is trying to give end users A little bit more information about what's happening, right?
Lisa Jung 00:24:56 Nice.
Dan Gomez Blanco 00:25:01 Yep.
And if this can be used by the SIG as well, in any way, for example, if you see something being completed.
Here.
Maybe something to… Go and find end users that… would be interested in talking about… I don't know.
declarative config, or… or Arrow, or… I don't know, maybe reach out to the team, and then go like, hey, you know, we've… Is it… I don't know, if we find something is completed, maybe it's worth finding an end user as well that has been using that, or that's been already using that in prod?
Lisa Jung 00:25:40 Nice.
Dan Gomez Blanco 00:25:40 Could be a cool… Cool thing to do.
Reese Lee 00:25:51 Okay, so there's this roadmap, and then there's the…
Dan Gomez Blanco 00:25:55 Yeah, that's sort of date is. That is… yeah, this is… we'll probably need to change this at some point. Still almost like, you know.
Inline, but yeah, we need to update this.
This was a requirement from him.
Graduation as well, to have a bit more of a… You know, process around this, around how do we come up with this roadmap?
Reese Lee 00:26:20 Yeah…
Dan Gomez Blanco 00:26:23 So the way that these… if you wanted to know the way that these projects are synced, is… If you open the community repo, the hotel community.
Reese Lee 00:26:37 Hold on a second.
Dan Gomez Blanco 00:26:45 And if you go to 6.yaml, and there's a file in there… 6.yaml.
Now, every SIG… Not every sake, so… but see, the first one, line 35.
Yeah, so, now there's a new field here that says, these are your roadmap projects.
And then you can… a SIG can have more than one.
You just have to give it the ID.
And then the rest is… happens automatically.
It's added to the… to the roadmap.
It can start to get synced, and whatnot.
Reese Lee 00:27:22 Gotcha. So the roadmap meaning this one.
Dan Gomez Blanco 00:27:25 Yeah, that one.
Reese Lee 00:27:26 Got it. Okay.
Dan Gomez Blanco 00:27:28 Because the one in the website hasn't been updated in a long time.
Reese Lee 00:27:33 Yeah…
Dan Gomez Blanco 00:27:39 Cool.
Reese Lee 00:27:39 Okay.
Dan Gomez Blanco 00:27:40 So this one's gonna be replaced by this…
Reese Lee 00:27:43 Or something that references this…
Dan Gomez Blanco 00:27:46 Yeah. Yeah, well.
Reese Lee 00:27:48 Got it.
Dan Gomez Blanco 00:27:49 We're just basically missing a few… we wanted to put more things in this before, and dates as well, for the last three, like…
Reese Lee 00:27:57 Yeah.
Dan Gomez Blanco 00:27:58 you know, Just so we get, Yeah, so… I haven't seen that comment, hasn't you?
I'll respond to that. But yeah, so I think, The ones that don't have dates will… or the ones that have, like, dates that… past. We need to update it, get it into a shape that we're happy to share, basically.
Reese Lee 00:28:26 Oh, that's cool.
Dan Gomez Blanco 00:28:28 I don't think it can be shared.
super widely now, but I just wanted to bring it up here so you're aware of how this works.
Reese Lee 00:28:36 Oh, no, that's cool. Like, I think it would still be helpful for end users to have, like, a… More general, something like this as well.
to this.
Dan Gomez Blanco 00:28:47 Yeah, that's a good idea.
Yeah.
Lisa Jung 00:28:51 So is every project accounted for in this roadmap?
Dan Gomez Blanco 00:28:55 At the moment, every project that is in the community projects is accounted for in there.
Reese Lee 00:29:03 Back to that.
Lisa Jung 00:29:05 And when will this become, like, public to the end users?
Dan Gomez Blanco 00:29:13 probably, we're hopefully aiming for KubeCon, to try the… The, to drive the… hopefully we can use that to drive the slides as well, that we're normally doing, like, hey, this is what's happening in a hotel.
Lisa Jung 00:29:26 This is awesome, Dan.
Dan Gomez Blanco 00:29:29 It goes.
Reese Lee 00:29:31 Yeah, that's pretty sweet.
Lisa Jung 00:29:32 Yeah.
Reese Lee 00:29:34 It's pretty sweet, but also it's, like… A lot, if you're not used to…
Dan Gomez Blanco 00:29:39 Yeah.
Reese Lee 00:29:41 Looking at this format.
Dan Gomez Blanco 00:29:44 There is the other one, there's a… I guess there's a table format as well, but…
Lisa Jung 00:29:50 So…
Dan Gomez Blanco 00:29:52 Also, some of the names are a little bit, like… You know, sampling sake, that's… So what is it trying to deliver? I mean, I would like to move towards that, you know, what is it trying to deliver?
Reese Lee 00:30:06 Yeah. Yeah, some of this is, like…
Dan Gomez Blanco 00:30:09 I mean, because some of the Kate semantic convention is great. I mean, that's… You know what you're getting after that's done, which is the semantic conventions, right?
But…
Reese Lee 00:30:18 Yeah.
Yeah, clearer titles.
would be helpful.
For sure.
Dan Gomez Blanco 00:30:27 But, you know, one thing at a time, I think.
Reese Lee 00:30:29 Yes.
Yeah, no, this is already, like, a lot.
of progress.
Cool.
Dan Gomez Blanco 00:30:40 Yeah, thanks for showing this to us.
Yeah, as I said, probably not something that can be… Widely shared now, but soon.
Reese Lee 00:30:51 Let's select it, let's select it.
God.
Dan Gomez Blanco 00:31:05 So, the other one is, so as you remember, now we've got And… that post that Andrea was showing.
As in, we've got a document in the end user docs.
And we've got… About issue participation.
And we've got, yeah, so there's one, and we've got guidance in the… for maintainers.
How to use… Thumbs up.
to… You know, you can go to a repo, and then… T… M… You know, what the issue… the issues and the thumbs up of, or sort issues by the number of thumbs-up reactions.
So if you go to issues.
Reese Lee 00:31:56 Nope.
Dan Gomez Blanco 00:31:58 And you go to… on the right-hand side, you can sort by newest, or you can sort by…
Reese Lee 00:32:03 No.
Dan Gomez Blanco 00:32:06 Reactions?
And then, yeah.
Reese Lee 00:32:11 Confused.
Dan Gomez Blanco 00:32:14 Right, so yeah, so the idea here, I mean, this one probably is not the best example.
But what I wanted to share is that end users and maintainers, and everyone's been, like.
If you open the… the image that was there.
was that I did a bit of… Data crunching.
Nope.
Yeah, so… And, you can… well, you just need to see the trend going up. We are getting more… Likes.
on all of our repos. So what I did was I ran something that will… Take the number of… There are a number of issues.
Now we're upvoted.
Per day. Or, no, per week, this is per week.
Hmm… Per repo.
And, yeah, there is a trend, which means that people are actually upvoting… upvoting issues more.
Reese Lee 00:33:11 Oh, sweet.
Dan Gomez Blanco 00:33:12 Which is good, good to see, because that shows more engagement, right? Especially in the, in the collector contract.
Reese Lee 00:33:20 Yeah.
That seems to be far.
Dan Gomez Blanco 00:33:24 the one that, yeah.
The one that takes most of them.
Mmm… One of the things that I was thinking is that this is something that I wrote as a script that I ran, like, locally.
Not… not too complicated.
Is that it would be cool to run this on a schedule.
So that we can have these numbers.
As something that we can look at on a daily basis.
You know, So… but I don't have the bandwidth to do this. To automate it. I mean, I did the script, so I might open an issue.
I will open an issue at the end user sig, and then… If someone's up for, like, you know, working with, And with the infrastructure sig, to deploy that.
into… I think we've got some resources in OTEL.
Someone could deploy it.
And run it.
On a place where, yeah, we can visualize it.
That would be good.
I mean, I might have bandwidth in 3 months, but yeah.
Don't know.
And I can share the code, on that.
Yeah, sorry, that took a long time for me, that's… that's me.
Reese Lee 00:35:05 No, these are all great updates. That's really cool.
It's cool to, like, finally see, you know.
Graphs and numbers from, like, this work that… Yeah.
Been talking, like, working off for so long.
Dan Gomez Blanco 00:35:22 alone time.
Reese Lee 00:35:23 So.
Dan Gomez Blanco 00:35:24 Here's a question. There was a… Let's see if I can find it.
Reese Lee 00:35:29 I think I should…
Dan Gomez Blanco 00:35:30 Put this, or we… we should put this, link somewhere, or basically document how we're planning to use these reactions as an end user's sake. So I think we talked about that before, as in… If you look at the most voted things, That… across the projects.
That were closed.
issues that were recently closed that were unvoted for a lot of people. Wouldn't that be a… Good way of, like, trying to find I don't know, end users that upvoted that, or that are using that.
If we could… And then do a session on it?
Reese Lee 00:36:12 Yeah…
Dan Gomez Blanco 00:36:16 So… Maybe that should open another issue for that.
I don't know, come up with a… An idea of how we can use it?
Reese Lee 00:36:32 Yeah, this is interesting.
I like the one that you just said.
Cause I think there's… Some interesting things we could find out from… That for sure.
would we have to do… if we did that, would we have to do something like… I mean, I guess we can just reach out to people and see if they're, like, okay with… Being interviewed, or if they're interested in doing the session.
Like, it's not… yeah.
Dan Gomez Blanco 00:37:11 Can I share my screen.
I think I found it, So, yeah, so this filter here… Gives you the reaction, so it's sort by reaction, things that are closed, issues closed.
Sort by reaction.
By thumbs up.
And now we're closed.
After… The 1st of January.
There we go.
So, I knew that hunt is somewhere, I'll link it in there.
So… yeah, so what you see here is then… Maybe… maybe close or not.
So, I think it'd be interesting to follow up on some of these, maybe.
Oh, you know, by the way, we're doing this now.
Reese Lee 00:38:06 Yeah…
Dan Gomez Blanco 00:38:09 Some of them are, like, expected, almost.
But some of them are like, this was voted a lot.
Visiting.
And if you open it…
Reese Lee 00:38:19 Burgeoning question.
Dan Gomez Blanco 00:38:22 It's got 17 votes, and that was closed.
So clearly, like, you know, small thing.
Potentially.
Yeah.
So I'll put the link here.
But if anyone has got any other ideas how we can use that…
Reese Lee 00:38:53 Yeah, I'll… I'll… Have to noodle on this.
And yeah, if anyone else has something… That they would like to see from this data.
Definitely share it.
Dan Gomez Blanco 00:39:12 Or in any way, you know, I think there's… I think this opens, like, you know, for example, that thing about, like, measuring the most popular Issues, or the most… the activity and repos by… Thumbs up, that could be.
as another use, right? So… Love it.
Reese Lee 00:39:35 Yeah, it'd be interesting if we… I mean, it's so broad, right? But it'd be interesting if we could… Somehow find, like.
I don't know, general… themes.
Dan Gomez Blanco 00:39:51 Like, you know in Reddit, when you get the most controversial?
Lisa Jung 00:39:55 He's like… Is it possible to analyze the data to see, like, what is the most requested feature requests, or, like… Troubleshooting… stuff?
Dan Gomez Blanco 00:40:11 You could probably find… There is no standard across OpenTelemetry for marking things as, bug or feature.
So, an issue could be a bug, or an issue could be a feature request.
But some… but there is sort of, like… there's always, like, you know, different labels. There's a set of standard labels, but others, you know, different SIGs could be using different labels on issues to mark something that is a feature request, or a bug, or something like that.
Don't know.
Lisa Jung 00:40:45 I mean, this could be really valuable information for, like, certain sigs.
And we could analyze it and give them the info.
Dan Gomez Blanco 00:40:53 Of, like, what is the, the most voted stuff, or more… what's your reaction?
Lisa Jung 00:41:01 Yeah, if it's possible to kind of identify what are some common themes, and then if you could identify which sigs need to know about it, and then disperse the info, that could be another way to use this data.
Dan Gomez Blanco 00:41:12 Hmm.
Yep. I think, yeah.
That might require more… A lot more activity.
If we're seeing, if we keep seeing more engagement, then… So at the moment, I'm not sure if the population is that… that huge for that.
Lisa Jung 00:41:29 Gotcha.
Andrej Kiripolsky (Grafana Labs) 00:41:39 I have a question as well. Is it possible to look at the dashboard that you share the panel from, or is it, like, a private one?
Dan Gomez Blanco 00:41:48 It's, pr- it's, yeah, I just ran that in a… Yeah, it's some JSON data, like, displayed on a Grafana dashboard, so… Yeah.
something that I ran locally.
I've got the data.
Can you share that.
I mean, but anyone can run the script and generate it as well.
Andrej Kiripolsky (Grafana Labs) 00:42:12 Yeah, no, I was just curious if we have a… if we… I was just curious if, because I know that there is a Grafana instance for OpenTelemetry.
Or rather for CNCF, that… where, like, some data about contributions are displayed, so I was just wondering if this lives there as well, or if it's…
Dan Gomez Blanco 00:42:33 That's a good question. There is… One, there's a… there's a… well, there's two things, right? There's DevStats, and there is the Linux Foundation Insights.
the new stuff. But yeah, it doesn't have this.
M… I actually don't… maybe it may be worth asking if anyone knows… anyone that's working on that.
Linux Foundation Insights.
I don't know if the end goal is to get rid of defstats?
And then do everything in… LFX Insights.
But, are you familiar with, I'm still sharing my screen, right?
Reese Lee 00:43:16 Yes.
14 degrees.
Dan Gomez Blanco 00:43:24 Are you… yeah. In Edinburgh, yeah. Are you familiar with, with this.
So this is fairly new.
And this is generated for all projects.
Look at this, it's all green.
Excellence Health.
Reese Lee 00:43:45 Hmm…
Dan Gomez Blanco 00:43:46 For OpenTelemetry.
And you can see, like, some of the… Mmm… Contributors Leaderboard, this is for… let's look at the past 90 days.
Organizations, active contributors.
Reese Lee 00:44:04 Mmm!
Dan Gomez Blanco 00:44:05 There are some really cool metrics here, and popularity as well.
But we don't have.
Mmm… Mmm… Who knew?
something related to… to that. And there's a dev stats one as well, of course.
But yeah, there's a lot of, a lot of good data here.
Very nicely presented, as well.
Andrej Kiripolsky (Grafana Labs) 00:44:29 Can you share the link in the agenda? I would like to take a look afterwards.
Dan Gomez Blanco 00:44:33 Yep.
Andrej Kiripolsky (Grafana Labs) 00:44:35 Thank you.
Dan Gomez Blanco 00:44:59 Cool.
I think Adriana might not make it.
So… Yeah.
Do we cover these two?
Andrej Kiripolsky (Grafana Labs) 00:45:16 Yeah, I think it would be good, I think that's what Adriana, like, she mentioned to me and Ernest that it would be good to cover those.
Yeah.
Dan Gomez Blanco 00:45:27 Alright.
Andrej Kiripolsky (Grafana Labs) 00:45:28 I don'.
Dan Gomez Blanco 00:45:29 I don't know much about the fact… I saw the message from Austin, but I don't know much about this, Run a survey targeting Japan and the cloud-native hotel communities there.
They ask us to look at the adoption rates, what kind of content events they want, where they get their info.
This might be a good item for our initial collaboration with someone else.
M… That's from Adriana.
Andrej Kiripolsky (Grafana Labs) 00:45:58 Hmm… Yeah, and so we were discussing with Adriana and Ernest that Ernest might run one survey as part of the mentorship.
Just to, like, bottle test some of the guidelines that he will be preparing. So yeah, I think that would be a great idea, and I mean, like.
We'll continue talking about it, because I know that there are some other things to it that we discussed with Ernest, but yeah, overall, I think it's a nice one, and… If there is no other volunteer, I'll be happy to… I'll be happy to help with that one.
Dan Gomez Blanco 00:46:41 That sounds good. Do we know… maybe that would be a question for Austin, if he's got any… So, like, any connections on the cloud-native?
Japan… Sort of like… Basically, how do we get visibility of this?
M… Yeah, I don't know if I could… I could ask as well.
Does anybody here have any?
I guess… Any connections in… Or anyone that could help us?
promote this in Japan.
No more to do.
Reese Lee 00:47:27 We could probably talk to the ambassadors. I'm sure they have… connections to ambassadors, CNCF ambassadors in Japan.
Dan Gomez Blanco 00:47:38 It's a good idea. Or, like, in the region.
Reese Lee 00:47:42 And actually, Adriana is a CNCF ambassador.
Dan Gomez Blanco 00:47:49 We could also talk to the Japanese localization sites.
Lisa Jung 00:47:53 And see if they could help us out.
Dan Gomez Blanco 00:47:55 Possibly, yeah.
Lisa Jung 00:47:56 I can ping them.
Victoria Nduka 00:47:59 Another thing… Duh.
I'm thinking, like, When we post on this, on our socials, we could also target the… The time that… The, like, it's time when they're more likely to see Post about the survey so they can fill it.
I don't think that makes sense.
Or if anybody even heard you.
Dan Gomez Blanco 00:48:30 Yeah, so… I didn't, I didn't follow there.
Victoria Nduka 00:48:34 Yeah. So I said, like, another thing that… another idea I have is to… when we… when we… when we post about the… because we're going to run sub-service, right? When we make… Posts on our socials.
Dan Gomez Blanco 00:48:47 We schedule it at a time.
Victoria Nduka 00:48:50 Like, Japanese time, I don't know what the time zone is.
When they're more likely to sing and feel.
Dan Gomez Blanco 00:48:56 Yeah, yeah, that makes total sense.
Ernest Owojori 00:49:00 Yeah, sorry, I would like to ask a little bit question around that. So, is it going to be the first time where we are interacting with that particular community?
Dan Gomez Blanco 00:49:12 Targeting… Specifically, yeah, I think so. I think so.
Ernest Owojori 00:49:17 Okay, so, is there any way we can know how many Japanese or anyone within our community have feed our surveys in the past? I guess no.
Dan Gomez Blanco 00:49:27 Hmm.
Technical.
Ernest Owojori 00:49:31 Okay, so one idea that came to mind is, maybe… I'm going to check that with… Andrea and Andriana to check the nearest community, let me say, tech community that is related to OpenTelemetry that is happening in Japan, and probably find a connection of someone that is going to attend. Maybe that would be the best way to you know, let people know only. Like, I mean, secondary means anyways, then the primary means would be to try to reach out to the ambassadors, as Ree said, but I think, having someone's foot on the ground for the nearest community of events would make sense to… Rich people.
I don't know if you get what I said.
Dan Gomez Blanco 00:50:21 Yep, yep.
Lisa Jung 00:50:23 Good question for you. Is this survey gonna be in Japanese or in English?
Ernest Owojori 00:50:29 Oh…
Dan Gomez Blanco 00:50:31 I guess English, because I don't understand Japanese.
Ernest Owojori 00:50:35 Perhaps it'd be… yeah.
Lisa Jung 00:50:39 I think in order to increase engagement, perhaps we could, like, write it in English first, and then get the localization's help… team's help on translating it, perhaps? Because if I see a survey in a foreign language, I may not… be… I mean, surveys… taking surveys are, like, hard enough, but if it's in a foreign language, I think it might be, like, adding even more barrier.
And then we need to translate it back to English if we want to… Post it on our website or whatnot, but… Yeah.
Ernest Owojori 00:51:18 That makes sense. That makes sense to me, but I just started asking myself, hope we're not losing information due to translation, but I think if you have someone That is… and I understand the two languages very well.
And the volume of responses that we'll have to translate is also a theme.
Because you can imagine someone translating 120 responses, that's a lot.
Lisa Jung 00:51:46 Yeah.
maybe we could use, like, Google Translate or something, and then have the localization team to reviews to, like, lessen their workload.
Just making sure we're not saying anything crazy, yeah.
Ernest Owojori 00:52:02 Okay, yeah, that makes sense.
Maybe I will speak with, Andrea, Austin, and maybe, Austin and Andre, maybe we can have that as a fallback plan if the responses are low.
With English.
Because I think the stress of translating is also a thing, which is going to take time, so we want to be sure we have the problem before we actually Let's try to solve it.
Lisa Jung 00:52:29 Totally.
Yeah, and I think once you get, like, the template down for the survey, let me know, and then I could reach out to the SIGS and see.
If they could help us out with the promotion, and then maybe, like, checking on the translation and whatnot.
Ernest Owojori 00:52:46 Yeah.
Notated. Thank you.
Dan Gomez Blanco 00:53:11 Cool. Do we have enough to… Continue with the next topic.
Alrighty, so that's Adriana, that, again, There is an hotel in practice session with the folks from Bindelain.
Keeping it vendor neutral on September 24th.
I guess, I don't know why, keeping the vendor neutral. Yeah, I guess that's probably a reminder to everyone that…
Reese Lee 00:53:43 Beautiful.
Dan Gomez Blanco 00:53:44 when we… When we do sessions, Ordalent practice, or whatever.
Yeah. Especially when we've got vendors that join in practice. We need to remain yeah.
need to be… sure that we, yeah, that we're remaining vendor neutral, and we're talking about hotel, you know, specific.
features.
The vendors.
May or may not offer.
Reese Lee 00:54:10 Yes.
Dan Gomez Blanco 00:54:16 So you're gonna be creating the… The social… no, the…
Reese Lee 00:54:22 the media assets, and then once I have the thumbnail, then we can create the… CNCF community… Event.
Dan Gomez Blanco 00:54:34 Cool.
Mmm…
Reese Lee 00:54:38 Yeah, let me know if you need a hand.
Dan Gomez Blanco 00:54:40 I'm… not gonna be able to attend that one.
But.
Reese Lee 00:54:46 Okay, oh yeah.
Dan Gomez Blanco 00:54:47 We need help for… looking for help for social promos.
Is… Is there an issue for this?
Reese Lee 00:54:58 I did see one.
Dan Gomez Blanco 00:55:01 What did I say there, though, yeah.
Reese Lee 00:55:04 I have seen this shoe.
Dan Gomez Blanco 00:55:15 Can't see you here.
I'll post it.
Reese Lee 00:55:18 Oh, thank you.
Excellent, okay.
Dan Gomez Blanco 00:55:31 Coop.
Reese Lee 00:55:34 Yeah, once I get the media assets, I will… Share them, and then if anyone is interested in helping draft up some social promos and buffer, and… Our buffer count, that would be cool.
Or…
Victoria Nduka 00:55:52 Yeah, I can't take that.
Awesome, thank you for joining me.
Dan Gomez Blanco 00:55:56 Oh, we need to… I just realized we need to, update our… issue template. It keeps, mentioning X, which…
Reese Lee 00:56:05 Whoa.
Yeah.
Dan Gomez Blanco 00:56:08 LinkedIn, Blue Sky.
Mastodon.
Reese Lee 00:56:12 Passed on.
Does anyone know, do we have, Reddit? Is anyone on Reddit?
Dan Gomez Blanco 00:56:28 Yeah, interesting.
Because…
Reese Lee 00:56:31 like…
Dan Gomez Blanco 00:56:31 It's not a place I think of to go for tech stuff, but apparently there's, like, a lot of I do.
I do follow that, yeah. And Severin mentioned this to me the other day, If, it would make sense.
To include… to have an hotel… Account.
Yeah.
The question was, like, would that be, like, would we be in charge of moderating the OpenTelemetry subreddit?
Reese Lee 00:57:03 Ugh.
Dan Gomez Blanco 00:57:04 Like, you know, I don't want to be a moderator.
Reese Lee 00:57:08 Yeah, no, people…
Dan Gomez Blanco 00:57:10 Yeah. Although, you know, the OpenTelemetry subreddit is very, very nice. Like, there's no, I have not seen any… Anyone, you know, Having a spat over something.
Reese Lee 00:57:22 Oh, that's… That's nice.
Dan Gomez Blanco 00:57:25 It's a nice corner of Reddit.
Reese Lee 00:57:28 Yeah.
In general, I have to, like, avoid… The comments section of posts.
Ugh, yeah.
Dan Gomez Blanco 00:57:40 Yeah, but that's a good point.
And then I guess, you know, that would be a question of, like, if we have OpenTelemetry Reddit account.
Would that be… who would own it? I guess we've got the media assets, we've got… Well, the same, I guess the same with LinkedIn, or… YouTube.
It's like a shared ownership, almost, between end-user SIG and COMS SIG.
Reese Lee 00:58:13 Yeah, it would be interesting just to, like, get a feel for, you know, where people are.
Like, what channels do people use to get their… Yep. Technologies.
Oh, is that no longer… It's weird.
Dan Gomez Blanco 00:58:37 I mean, it does There's always posts… 1.3,000 weekly visitors, and openTelemetry… subreddit.
Reese Lee 00:58:49 Huh.
Dan Gomez Blanco 00:58:49 So it's not… not insignificant.
Reese Lee 00:58:52 Dang, that's so interesting.
Because, yeah, we did, like, a… we have a new social media manager at work.
And she was trying to get a feel for, you know.
Where we should invest our time.
And so we, like, just ran, like, a really, really informal survey, trying to find… figure out, like, where people… Generally go in, like, Reddit… Was, like, a top one.
Which I was like, oh, I do not think to go on Reddit myself for, like, tech stuff, but… It's a big thing.
Dan Gomez Blanco 00:59:34 I mean, my… I just saw this, and this is great, so I just need to share it now.
Reese Lee 00:59:40 Oh, no.
Dan Gomez Blanco 00:59:42 Yeah, good friend of Bella.
That's good.
Reese Lee 00:59:51 Holy cow, that's a huge mug, Lisa.
It's like your face has disappeared.
Lisa Jung 00:59:59 It's my souvenir from, like, 20 years ago, but, like, dude, I need this to keep up.
Is that…
Dan Gomez Blanco 01:00:06 Nope.
Lisa Jung 01:00:07 But coffee.
Andre was just commenting on it.
Reese Lee 01:00:12 Damn, that's… yeah.
Lisa Jung 01:00:14 I was like, whoa! I'm gonna be up all night, yes!
Dan Gomez Blanco 01:00:19 I just have one cup of coffee a day, I don't drink that much.
Reese Lee 01:00:23 Yeah, and it's like…
Dan Gomez Blanco 01:00:24 Fucking one liter mug?
Lisa Jung 01:00:26 Probably. Doesn't say.
No, it doesn't, but yeah, it's quite a big mug.
Reese Lee 01:00:33 Like, 30 ounces or something.
Lisa Jung 01:00:36 You just need one cup a day.
I do have to heat it up, like, multiple times, though, because I can't finish it before going cold, so…
Reese Lee 01:00:48 Yeah.
That's nuts.
Wait, so what is Severn… so Severin is, like, kind of looking into the Reddit thing? I'm just curious.
Dan Gomez Blanco 01:00:59 I think he mentioned that, and I think that was… that didn't go anywhere else, but… Yeah. Okay, yeah, I mean, I don't know anyone who wants to…
Reese Lee 01:01:08 do that, so… But, I mean, I guess we could, like, try posting, you know, just, like.
I could try posting from, like, my own account about, like, oh, we have this thing, and just see if we get any bites off it.
Okay.
Dan Gomez Blanco 01:01:29 Actually, no, I remember, just looking at this, Severin Deadpost.
One of the autonoming practice sessions, got…
Reese Lee 01:01:36 Oh.
It was like,
Dan Gomez Blanco 01:01:40 And he asked to be moderator of that… so, yeah, so, you know, there you go, Severin, volunteering to be moderator.
But he hasn't got an answer yet.
Reese Lee 01:01:52 Okay.
Okay, I guess I'll be checking out OpenTelemetry Reddit later today.
Awesome.
Well, that was a great hour, guys, thank you.
Dan Gomez Blanco 01:02:08 Yeah, thank you very much.
Alright, see ya, bye-bye.
Andrej Kiripolsky (Grafana Labs) 01:02:15 Bye!
