SIG: Go Compile Time Instrumentation SIG
Date: 2026-07-30
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Dario** 09:56 Holy shit.
**Aditya Vishe (ADITYA-CODE-SOURCE)** 09:58 on top of that.
This spot.
**Dario** 10:05 Give me a second, I will share my screen.
The other day, I joined through the other links, so I don't know why I failed today. And you?
Here we are.
Good morning, good afternoon, as we are around the wall.
Let's start. I'm going to facilitate, given that I don't see anybody from… Alibaba's, or CabiFi Present.
And actually… yeah.
I don't know if we can actually discuss the first point in the agenda.
About the long, sweet Instrumentation migrations, because that Alibaba's… Tool.
So, meanwhile, I would suggest talking about Azar's proposal for the Ecosystem Explorer integration.
**Azhar Momin** 11:02 So… Yeah, so we had proposed this… RFC regarding OTLC and Open Data Material Registry integration, and I was suggested by the open directory maintainers to… maybe the Ecosystem Explorer would be a better place for this, whereas in exploring the Ecosystem Explorer.
Side by side, and… Apparently, the main goal of Ecosystem Explorer is that they, instead of, having a handwritten, manually generated registry.
They automatically insert from the different repositories they currently have.
a system to install from the OpenTelemetry Go country.
And… They also have cool features, if you go to, I think it's explorer.opentermetry.io, can you open that?
Yes.
Yeah, so they have currently, the Explorer Small Java agent, and I think this would be cool if we have similar core.
Go Compile Instrumentation, because they have for example, the declarative configuration stuff in there, which is relevant to our upcoming LFX proposal, and They also have, for every release they have, The… the document, what telemetry is, Instrumentation liability, Emmet, and… stuff, so that would be cool for us. But the problem, I think, right now is Our initial proposal covered third-party repositories, so, people could, just add their repository to OpenTylement Registry, and OTLC would automatically pick it up. But, I don't see how, that would be possible for Ecosystem Explorer right now. Maybe we can explore it down the roads in the future, but right now, I'm proposing that we have a simple contract repo for all the instrumentations. We can maybe add third-party instrumentations in there, and… it would be easy for ecosystem explorer integration, and I wanted opinions on that.
So, maybe I missed some concerns on that.
**Dario** 13:35 Sorry, didn't catch the last part. Maybe what?
**Azhar Momin** 13:39 Maybe I missed some concerns on that, maybe.
there could be some problems, so I want to discuss and go into more, opinions on this.
**Dario** 13:51 So, the TLDR of this is that… We could have something like this.
And this is, something that we can contribute to.
Like…
**Azhar Momin** 14:02 Right.
**Dario** 14:03 Okay, what you're contesting here.
**Azhar Momin** 14:05 Yes.
**Dario** 14:06 Do we have an example? Are these examples?
what we are looking for. No, this is their Visit, their previous.
**Azhar Momin** 14:14 Bye.
I think, let me, try to find an example.
**Dario** 14:24 Yeah, an example would be great.
**Azhar Momin** 14:28 They have currently this, go watch it.
And, this automatically… like, yeah, he has linked there, the Go Watcher, and it, automatically infers the… Instrumentation in OpenTelemetry go country. So it solves two problems for us. First is we can have the artifact for the registry entries, and OTLC can automatically figure out the instrumentations from Ecosystem Explorer, rather than having, I mean, OpenTelemetry registry, as we had discussed previously.
So, this is first part, and the second part, we can then also have the UI, which is feature work, all of that. My initial proposal is just having the registry in there, so OTLC, so we can decouple the OTLC and Instrumentation lifecycle.
Within the Go Country repo.
Open telemetry, go Compile country.
**Dario** 15:35 Okay.
**Azhar Momin** 15:36 We have to create that.
**Dario** 15:37 Mmm, yeah.
But the…
**Azhar Momin** 15:42 Yeah, this was my proposal.
**Dario** 15:44 Okay.
Okay, I see, because this…
**Azhar Momin** 15:51 Okay.
**Dario** 15:52 is part of an ETL pipeline that clones a specific repository. So the proposal would be, like I said, creating a new repository with all the integrations.
And basically, just enhance this tool, just to check.
**Azhar Momin** 16:11 S.
**Dario** 16:11 the new one.
To me, sounds good, I don't know. I would… I would rather have this discussion also on a Slack, given that we are not many today.
**Azhar Momin** 16:25 Yeah.
**Dario** 16:25 I mean, we are a few, but mostly contributors, no maintainers.
So, I think it would be good to just double-check this with, with maintainers in the Slack.
**Azhar Momin** 16:37 Right.
**Dario** 16:37 Or maybe in another meeting next week.
Or whenever it happened, but we need to make sure that we are present.
Okay.
Yeah, from my point of view, it sounds good. It sounds like the reasonable thing to you, provided that there are… there is existing tool in there.
Doing something very similar for another repo.
**Azhar Momin** 17:04 Sounds good.
**Dario** 17:07 Okay, let me just summarize this on… on the dock.
Also, everybody, if you can write down your… Name… the dog, that would be great, so I don't have to… Write all the attendees list.
I'm going to just do this, that… Okay.
Steep.
My headphones are failing. Okay.
Escape the long, sweet.
This, migration… Also, okay, stars… -Oh.
Way to integrate.
Could be great.
Yeah, that's my dream… Sorry, what was the name?
**Azhar Momin** 18:17 on fire.
**Dario** 18:18 Go Compile. Thank you.
**Azhar Momin** 18:20 How can I do?
**Dario** 18:23 So we… Can be, tracked by… Jeez.
Excuse him.
Dude.
I'm gonna think… oh, no, that's the Google box.
Okay.
Yep.
This is a… this is a summary, okay? If I'm missing details, don't hesitate to add in the notes.
Okay.
Yeah, and you suggested to… So I'll check this on… this block.
Us maintainers are not perfect.
Right now.
In addition. Okay, cool.
Anything else?
That we want to discuss regarding this.
**Azhar Momin** 19:23 Okay.
If we can maybe… talk about some… there are some new people here, and there are a lot of new PRs coming in, and yeah, some people are also helping with the reviews. It's also great, but there are right now, also many duplicate PRs, and… -Oh.
It would be, great for new contributors if they can.
hold on for creating new PRs and maybe, help a little bit with the deals. There are already people helping, but it would be great if we can Right now, hold a little bit on those.
**Dario** 20:07 Okay, so… Okay, but regarding the explorer point, I think we are good here.
**Azhar Momin** 20:15 I'm done. Yeah, yeah.
**Dario** 20:17 Okay.
And are you suggesting to do some… Round of interventions with the present people, and maybe talk about… PRs and stuff. Okay, sounds good.
Okay, is your term.
Who wants to talk, who wants to comment, or discuss any… anything regarding the current work, big workload that we have in the repository.
**Karthik** 20:57 Hi, guys.
I'm Karthik, I'm from India. I'm new to this OpenTelemator, actually. Thanks to LFX, I found this awesome project. I was searching for a new CNCF project to contribute to, actually. I'm a reviewer in a CNC sandbox project, right? Now I've been searching for new projects to contribute, I'm… I found this… this is actually good. I'm trying to wrap my head around some concepts here, and most of them just goes above my head, it's… Kinda… new for me, but it's good. I'm creating the docs. I'm seeing so many people are opening new PRs and stuff.
I don't know how they managed to understand the concepts, but I'm, so faster, but I'm getting there slowly. I've been seeing Azhar is doing a great job around here, so I'll get there eventually.
Good to be here.
**Dario** 21:52 Glad to hear that.
And yeah, it's… it doesn't seem like a complex project, but it's quite complex under the… under the hood. So, yeah, don't worry, take your time.
**Azhar Momin** 22:04 If you have, any questions, you can ask, us on the Slack or GitHub directly, we'll be happy to help you.
**Dario** 22:11 Yeah.
**Karthik** 22:12 Yeah, sure, thank you.
**Dario** 22:15 Okay, I see a hand raised. Please go ahead.
**Satyabrata Mohanty** 22:28 Hello? Like, can you hear me?
**Dario** 22:31 Yep.
**Satyabrata Mohanty** 22:32 Yeah, hi, myself, Satya, I'm from India. From last few days, I've been reviewing PR, like Azhar… I've been talking with Azhar also, regarding this PR. So, in the PR, I have been around… I have reviewed around more than 15 PR. So, in there, I found some issues, like.
There are some, basically, AI-generated PRs out there, and also.
not requiring, like, unwanted comments are also getting pushed to the codevace, and also some linting things that AI is also trying to generate, and people are pushing it to the, like, in the PR, they are showing, so I think this, should be any workflow, should we maintain that, any… linting things from our side, we shouldn't do that. In the PR, the person shouldn't do that. It will be directly done by the workflow system only. And before that, the linting things that is managed by our inner codebase only, that basic thing should be taken care of by the PR author. I think this should be taken care. Like, those AI-generated things that are getting pulled with the PR, So, I think this should be also taken care of.
And also.
Like, there are, yesterday I found out, like, two, three PRs are there, there are just simple duplicate PRs. Someone is raising the issue, and other two, three peoples are raising same PR only, and that should be closed immediately, I think.
They should be done.
Among the contributors who are creating PR.
This should be done also on immediate basis.
No, or else the PR account will grow. As you can see now, it's currently 89. It was around 80-something, and more 9 PR has come. Yesterday only, I found out, like, 2 to 3 PRs are the same issue, same… thing they are trying to solve, and they didn't check out the PR list that is… there is any pending… such PR pending, so they created another PR, and this would create a huge, huge rise in the PR count. So this should be fixed, I think.
**Dario** 24:45 Regarding those PRs that you mentioned that were AI-generated, I mean, a lot of them probably are, but the ones that got your attention, can you share links on Slack? Just to make…
**Satyabrata Mohanty** 24:57 I am sharing with Azhar… I'll share with Azhar or those peers.
Those are… those I've been reviewing. It will be easy for Azhar also to approve that if everything is fine, because Azhar will start from the scratch. That will be good that I review them, and also put my comments there. If it looks good to me, then Azhar can also check once… directly check that, and approve those changes.
It would be easy for him also.
**Dario** 25:22 Okay, yeah, I guess you're referring to… let me share my Slack.
To this, right?
**Satyabrata Mohanty** 25:32 Yeah, this has been some… One second, I'm, sharing some… yesterday only. I think the guy has closed that PR.
80, 855. It is PR number 855 and 862. These are same PRs. 855 PR was the earlier PR.
the Pierre Rouses rest before the age 62.
So, I told him that to keep the 855 here.
**Dario** 25:59 Okay.
**Satyabrata Mohanty** 26:00 And closed that A62. And the guy closed it. The guy closed that PR. And also, I'm checking more of the subscriber PRs, because reviewing is all one thing, and closing these PRs, the duplicate PRs, is more important, I think.
First, so that will be easy for us to also review the PRs, because multiple PR sent things will be, again and again, going through same PR.
That would be not illegal, also.
I think… We should once go through all the PRs and close the duplicate, and then continue… continue the new contributions, or… reviewing those things.
**Dario** 26:39 Okay.
Okay, gotcha.
Yep.
We'll check this offline, okay? Asynchronously on Slack. It would be… much easier, and we can have more time for discussing other things that are relevant for the repo.
**Satyabrata Mohanty** 27:00 Yeah.
**Dario** 27:02 Thank you, anybody else wants to… Discuss anything?
**Anand Mishra** 27:08 Hi, this is Naran Mishra, am I audible?
**Dario** 27:12 Nope.
**Anand Mishra** 27:13 Hello, Rishi Anandisha, I'm from India.
Over the past few days, I've been reviewing OpenAI Instrumentation, reading the registry.
integration RFC, and, understanding how Octel discovers and applies Instrumentation.
I also spent some time auditing the middleware and streaming implementation, looking into that area, such as request handling.
And, providers detection, potential subdomain.
spoofing scenarios.
and handling some unbounded SSE lines in streaming response. I am still validating my res- observation.
Before proposing any changes or opening any issues. Right now, I am looking for a good first contribution, but I am taking some time to understand the architecture before opening an APR. I don't have any blockers at this moment.
But, I made some architectural guidance For this codebase.
Can anyone help me with that?
**Dario** 28:20 Yeah, feel free to ask questions on Slack. If you can't share Anything that we can see… it would be easier for everybody to give you the guidance you require. Me, Kamal… Kamal is out of office, but Azhar to… We can do that, we can help.
**Anand Mishra** 28:41 Thank you.
**Dario** 28:45 Yeah, okay.
Hmm… Who's next?
I guess we don't have the next person. Yep.
I heard somebody.
No?
If you want to talk, please raise your hand through… through Zoom, so we make… we are sure that we are not hearing some artifacts or what, but… In the meantime… So, we have discussed… a self-proposal, I think it's the right way to go.
But again, let's double-check with some maintainers. The long-free migration, I am not sure what they wanted to discuss specifically.
I don't know. I remember that there was this issue open, but the details weren't fulfilled, so… I don't have more information.
If there isn't anything else to discuss, we can cut the meeting short, or we can answer questions.
If we are able to… Whoa.
Whatever you want.
Okay, yep, go ahead.
**Aditya Vishe (ADITYA-CODE-SOURCE)** 30:40 Oh, hello, sir, I'm Adityitya from India.
So, hi sir, like, I want to know about my PR8012, like, you can just check it out.
Also, I have some doubts in it.
**Dario** 30:58 Mmm, okay, you have 3… which one in particular?
**Aditya Vishe (ADITYA-CODE-SOURCE)** 31:02 81.
**Azhar Momin** 31:04 Yes, I… Was actually trying to review it, but, No, I think they're, and the other one, the portal.yaml one.
I will try to review it soon. Actually, I was going to work on a similar thing, but you worked on it, so that's great, I'll try to… Look into it soon.
**Aditya Vishe (ADITYA-CODE-SOURCE)** 31:32 What about, like, my other PRs? Like, is that good, or can I change something?
**Azhar Momin** 31:38 Yeah, there is a huge influx of peers right now, so… And, as Jaymon has already talked about this on Slack, the maintainers are limited, and, voluntarily, reviewing the PRs. We'll try to go through them soon, but right now they're, Huge number of PS.
**Dario** 32:13 J.
Yeah, I need a little bit more time to… to check this.
Okay, so I'll prioritize these PRs. I will also… okay, I am reading the chat. I will also DM you the list of PR after reviewing, which will be managed for the team. Thank you, appreciate that.
Okay… Yeah, because I'm not even… about those PRs, I'm not even aware of this one, so… I don't remember many things in our heads.
Okay, yeah, thank you for bringing this to our attention. We'll do our review as soon as possible.
Anything else?
We still have 30 minutes.
But if not, we can just cut the meeting short and get back those precious 30 minutes back.
Going once… Going twice.
Once rice. Okay.
Then, if there is anything else, we can talk about it on Slack. Thank you very much for attending. Azhar, tell me if you want to meet later. We can talk more Specifically your proposal, or if you consider that you don't need that, it's okay.
**Azhar Momin** 33:51 You know? Thank you, thank you.
**Dario** 33:54 Okay, well… See you all.
**Azhar Momin** 33:56 Goodbye.
**Dario** 33:57 Thank you very much.
