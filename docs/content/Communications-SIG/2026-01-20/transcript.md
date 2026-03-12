SIG: Communications SIG
Date: 2026-01-20
Duration: 64 minutes
Zoom Recording URL: https://zoom.us/rec/share/V61RpO7TCuIPkDRY1IU4PkQT7EAMIv3ofkSM5rMhqQYxTP8QXRQnqmWROVoG5jOB.7Ijzy52mROwJalTL
============================================================

## Zoom Recording Transcript

Patrice CNCF 00:04:08 Hello, hello, good day.
Marylia Gutierrez 00:04:09 So…
Tiffany Hrabusa 00:04:12 Hello.
Who is that?
Patrice CNCF 00:04:16 Right, I was… I guess we don't want notes, right?
Tiffany Hrabusa 00:04:24 Yeah, I don't think so.
Patrice CNCF 00:04:37 I don't know if I have to write directly…
Tiffany Hrabusa 00:04:44 It looks like it disappeared.
As a participant, I don't know.
Severin Neumann 00:04:51 Hey, good morning, good evening.
Tiffany Hrabusa 00:04:53 Yes, I'm…
Patrice CNCF 00:04:57 Still says the meeting's being transcribed, I don't know.
Do you know, Severin, do you know who Bogdan Nikole is, and who turned on read.ai for meeting notes?
Severin Neumann 00:05:18 Hmm? Where is it, like…
Patrice CNCF 00:05:20 Well, before you came in, So, let me… It's okay, it should be off.
But we should find out. How do these people just turn things on?
Anyhow, we seem to have, Lots of things to talk about, so let's not worry about random people turning on AI bots to…
Severin Neumann 00:05:48 I think it's just an AI bot that joined that meeting, right, and you can You can throw them out again.
Which is still rude, I think, that it's like, hey, here's a.
Patrice CNCF 00:05:59 Exactly. Good.
Severin Neumann 00:06:00 Yeah, anyways.
Patrice CNCF 00:06:03 So I asked them to leave.
Sophia Solomon 00:06:14 Happy 2026, everybody. Bye. Sorry I couldn't make the last meeting.
Severin Neumann 00:06:18 No worries.
Patrice CNCF 00:06:19 Hi, thank you. Happy New Year.
Severin Neumann 00:06:38 Are we missing anybody, or… Here's…
Patrice CNCF 00:06:43 Fabrie said he… May or may not come, so… Yeah.
Maybe we just proceed?
Tiffany Hrabusa 00:06:52 Sounds good to me.
Severin Neumann 00:06:56 Yeah, let's get started.
Tiffany Hrabusa 00:07:02 Patrice, you're.
Severin Neumann 00:07:03 Yeah, sorry, Tiffany.
Patrice CNCF 00:07:06 The first item, is something we brought up in November, which was to, It would have been nice for February to be here, because I think he was excited about this prospect of us Fixing, planning, being proactive in terms of what we want to work on, since, yeah.
I don't know that we necessarily want to spend a lot of time. Maybe I just wanted to bring it up to say we had… oh, there's… Somebody's here.
Fabrizio Ferri Benedetti 00:07:39 Go there.
Patrice CNCF 00:07:40 Hello, hello.
So maybe, first item, is to talk about priorities for this quarter. I've started using the quarterly milestones, putting things in there.
I guess I wanted to bring back to our attention that we had Wanted to be proactive and set priorities for the quarter so that we can Make meaningful contributions to improving the website and the documentation.
I don't know if we want to spend… A few minutes… Just throwing out ideas for top items for the quarter, or we just think about it, and next meeting we'll put together a list. Of course, it's not… it's something that'll be fluid, Hmm.
I guess… Faberizio, you just kind of jumped in and, revamped the website, or led that effort, which, by the way, is phenomenal. Very glad to see that.
finally land.
So, I guess that's one example of the type of work that we can.
Fabrizio Ferri Benedetti 00:08:54 Yeah. Schedule.
Yeah, something I would like to tackle in this quarter is actually in the projects folder, which I don't know if everybody is aware of its existence, but it's about the consolidation and filling the gaps in our language instrumentation docs.
So that, that will be my next goal, maybe, possibly I will bring in, like, a new contributor from Elastic as well to help out, so… But yeah, it's, it's defined there. Like, I find it quite useful to always have that project file there available.
Patrice CNCF 00:09:32 Oh, that's the project folder in…
Fabrizio Ferri Benedetti 00:09:36 project folder, yeah.
But I don't know, I don't know if we need, like, now, like, a subfolder for completed projects, because now that the landing page one, for example, could be moved.
Be right back.
Patrice CNCF 00:09:51 Okay.
Diana Todea 00:09:56 Hello, I'm… Here as well, after a long time.
Patrice CNCF 00:10:01 Aye.
Severin Neumann 00:10:02 Yeah, no.
Diana Todea 00:10:04 No.
Sophia Solomon 00:10:05 Hi, Diana!
I see it.
Diana Todea 00:10:07 Hi, Sophia.
Sophia Solomon 00:10:08 How are you? Good, how are you?
Diana Todea 00:10:12 It's nice, yeah, good, good to be here and talking about OpenTelemetry again.
Severin Neumann 00:10:23 I don't know, do we want to give Fabrizio a little bit of time and maybe move on to the other topics, and maybe circle back to it?
Patrice CNCF 00:10:31 We… we could do that. Actually, I would say maybe we can circle back to it the next meeting. I don't think we necessarily need to spend time on listing things right now here. Yeah, because there are a lot of things to cover, so…
Severin Neumann 00:10:45 Yeah, our agenda is really full today, so I want to give… yeah, yeah.
Tiffany Hrabusa 00:10:49 Yeah, I think before we move on, though, everyone should just maybe spend some time over the next two weeks thinking if there are any major projects that you want to prioritize, in the docs repo, so that when we come back next time, it isn't another, okay, nobody has ideas, so let's just push it off again.
Patrice CNCF 00:11:07 Sounds good Thanks.
Next item is about, at least among us deciding.
Some criteria for… Using the good first issue label or not.
Again, maybe it's something that we want to think about in the next two weeks and come back with concrete proposals. I want to be mindful that we don't label issues that offer, too much of a challenge for newcomers, because the tendency will be for them to just… throw the issue at AI, and let AI do the work. So… that's why I want to… I want us to think a bit more carefully about good first issues being something within the scope of what a newcomer could do without necessarily the use of AI.
That was, the thought process here.
Although, if you may… you may have noticed, we've updated the ER checklist that submitters need to check. It's a bit stricter now in terms… or more accurate now in terms of them, admitting to whether they use AI and whether they have the domain knowledge to validate the PR, which is important.
That reminds me, I think I'll add an issue to, the meeting today.
we should… decide what to do with people who submit PRs.
In which they claim there's no AI content, but clearly there is.
As has happened with certain people who submit language translations, but…
Marylia Gutierrez 00:13:13 Yeah, it's funny when they had, like, something for, like, Portuguese, and then you reply to them in Portuguese, they're like, oh, sorry, I don't speak the language, but they also didn't mark that they use any tools, so it's like.
Severin Neumann 00:13:24 But, yeah.
Patrice CNCF 00:13:27 Exactly.
Marylia Gutierrez 00:13:27 Yeah, I just had, like, a spirit that came to me. I was able to speak Portuguese, but now they left.
Patrice CNCF 00:13:32 Just for a moment, yeah.
Fabrizio Ferri Benedetti 00:13:34 Like, oh, I like the sound of it, but yeah.
Marylia Gutierrez 00:13:39 Yeah, so for the… when I notice this on, like, the Portuguese one, I usually tend to tell people, like, yeah, we are not gonna review yours, because usually there's a lot of, like, nuances, and they… I know that I'm gonna have to, like, review every single thing, so I just say, like, oh, I just encourage them to look something on a language they… Know if there is a caution for it, or, like, find another issue that makes more sense for them, not necessarily on localization, but I just tend to say no.
Patrice CNCF 00:14:10 Good.
Tiffany Hrabusa 00:14:13 I haven't had a chance to, use the… The new resources as, like, a… support system. I haven't had any AI PRs just yet, so maybe I'll come back with some feedback once I have a chance to put it into action.
Marylia Gutierrez 00:14:34 Yeah, that is something we are also looking into other things, because that is… this is not the only, like, repo that this is happening. There is a lot happening all around, and you can clearly see, like, the responses as well. We're just like, I think you're using it right, and then replying, you are correct! You used AI to the reply as well, but… We are trying to make… create, like, maybe more guidelines in general, but definitely it is a problem all around the repos.
Patrice CNCF 00:15:11 Okay, I guess we've, gone… gotten slightly off-topic, at least for the good first issue, in terms of talking about AI, but all good. Yes, agreed. Thank you.
I suggest we move on to the… Next issue, although, which is also mine, Probably at this point, I… Assume if anybody objects that we want a solution that makes the registry more manageable.
Which I don't think anybody would. That particular issue was just to bring to light maybe some ways in which we can help automate and curate registry issues.
A registry entries becoming stale.
Severin Neumann 00:16:06 Didn't we have an enforcement for that? I mean… I thought that…
Patrice CNCF 00:16:12 good… Good question. But I don't think it necessarily ties into link checking, because one of the things that happens is that the links in the registry Some registry entries will become stale, and unfortunately.
Not everybody is good at setting up redirects, so that… We can at least get to the content.
Severin Neumann 00:16:35 I mean, we… yeah, I mean, we… I think I… I enforced the author… which is not necessarily a person, right? Sometimes it's, like, Microsoft Open, or something like that, or OpenTelemetry Authors.
My… I think the bigger question is, like.
I don't know how long, like, we will… probably longer than we hoped for, like, we'll have to registry, so… Jay, I see that, like, you… you probably stepped away for a minute.
But I don't know, I mean, if this is really a problem, or if this is something where we say, like, hey, this is something we can fix with the Ecosystem Explorer eventually, yeah, I don't know.
Jay DeLuca 00:17:23 A concrete solution doesn't come to mind immediately. I think this is an issue that like, the Ecosystem Explorer, I think, will be a little bit easier, because we'll be… at least for a lot of it, we'll be scraping directly from OpenTelemetry-type resources, where I think, like, probably more of the challenges in this space come from third parties, or…
Severin Neumann 00:17:47 Yeah.
Jay DeLuca 00:17:47 Unmaintained libraries and things like that.
I think it's reasonable for us to set some kind of bar where, like, if someone from the community, whether it's the original person who committed it, or someone who might be interested, isn't able to maintain it, then we just drop it.
Because… Yeah, I don't know, it's tough to… it's hard for me to imagine even putting, like, a single person as, like, an owner on some of these things.
Patrice CNCF 00:18:20 Well, as Severin mentioned… as Severin mentioned, we… Require, at least that somebody identify themselves as a custodian of the registry entry, and Maybe we need to enforce an email contact?
Severin, so that at least we can write Or some way that we can contact the person How do we know that the entry becomes stale? It's usually when links to their documentation or to the product disappear and get 404s.
Maintaining the ref cache, which is essentially external links, is a lot of work, in particular because there are a lot of registry entries.
And some people seem to be just driving by, oh, we kind of support hotel, and then the product disappears, and then we're stuck with trying to figure things out. So that was the background in terms of trying to automate this to some extent, and Probably mention up front our policy to say that If your website goes, or your docs go stale, you have a month.
to update it, otherwise we'll just drop it from the registry. I mean, thinking about users who… there's already a lot of entries in the registry, and it would be frustrating for users to think that there's some neat Artifact there that… Turns out to not be available anymore.
I'd say, maybe Izzy Todd and I can look into this, Eventually.
Severin Neumann 00:20:00 I mean, just to throw in one more option, I mean, if people do not provide a contact, we just remove it the moment it's stale.
I mean.
Patrice CNCF 00:20:09 Okay, I like that.
Severin Neumann 00:20:11 The thing is with, like, enforcing, like, hey, give us… I mean, we do this with the vendors, with the email address, right?
But even an email address, are we really sending emails to people? And then, like, some of them give us info at vendor.com, and then it's, like, yeah, going into some random inbox.
So maybe we say, like, hey, if you… if you give us a GitHub handle that we can, like, associate with that, then we will tag you.
Otherwise.
And we just put this number in the rules, and… yeah.
Patrice CNCF 00:20:45 At the end, let's also think about, like, how much maintenance burden we want to have with that.
Yeah.
Kind of like what you're implying, which is maybe… Regardless if there's a contact, we could state up front as a policy that if Their resources become… inaccessible, the documentation links or the product links, that will just delete the entry, that it's their responsibility to be proactive. I mean, that would simplify our lives and make it more manageable and easier to automate.
And it pushes the burden… the responsibility on them, which I think makes more sense.
Severin Neumann 00:21:24 Yeah, and removing and re-adding an entry, I mean, there's no… there's no penalty on that if it's not there for a month or something like that, right?
Patrice CNCF 00:21:34 Right.
We feel comfortable with that sort of a policy?
Okay.
Jay DeLuca 00:21:44 It's just one last thought about that is, like, perhaps to the point about if they do provide a contact. Like, maybe we could have some kind of optional opt-in where, like, Like, if you give us your information, if we mark this stale before we delete it, we'll reach out to you. But yeah, don't make it required, but just give kind of, like, an… if you care about this and you want to stay in the loop.
You know, give us your information and we'll reach out before we nuke it.
Patrice CNCF 00:22:15 I'd say maybe in, in our… The information we provide about registry contributors say that we'll do that on a best-effort basis, but ultimately it would be their responsibility to be proactive when resources move. How does that sound?
Check.
Good.
I'll see which notes or documents we need to update.
To reflect that. Thank you.
Tiffany.
Tiffany Hrabusa 00:22:48 Andrj from the end user SIG approached me last week.
They are trying to figure out which surveys to run next, and they wanted to know if we were interested in, re-running the doc survey that we last ran in late 2024.
I have some thoughts about this myself, but I wanted to ask the wider group to see what, what your take on it is.
Patrice CNCF 00:23:25 I would share… when was the last survey? The exact… do you remember the date?
Tiffany Hrabusa 00:23:31 I don't remember when it was run. I know that I published the blog post in late December of 2024. I don't remember… I think the survey was September or October.
Patrice CNCF 00:23:43 So, without thinking about this too, too much, my kind of gut feeling is that it feels a bit too early. It's a lot of work for everybody, including participants, but if you're feeling that there's been enough Change in the docs that it warrants having the survey I guess on a yearly basis, or 18-month basis?
That… that makes sense.
That's just my… Off the top of my head.
Tiffany Hrabusa 00:24:11 Yeah, does anyone else… Have thoughts on it?
No.
I don't think we need to settle into, like, a regular cadence, necessarily. I don't think that's what they're looking for. Yeah, Severin, go ahead.
Severin Neumann 00:24:28 I mean, they're a lot of work, right? So we should not just do surveys for the sake of surveys, so… Yeah.
Tiffany Hrabusa 00:24:37 So what I told Andrage, from my own perspective, is that I would like to see the collector docs refactoring, and at least some initial OTEL blueprints work.
Be published and kind of sit for a little while before we run the survey again.
But that's kind of from a very, like, two projects that I'm working on that I know will hopefully make, a big impact on users, so… I'm open to running it earlier, if anyone really wants to push for it, but I think that, for now, we could probably push it off.
Sophia Solomon 00:25:16 Do… was there a certain part of the docs that, Andre wanted to… Target for the survey, or…
Tiffany Hrabusa 00:25:25 No.
Sophia Solomon 00:25:26 in general.
Tiffany Hrabusa 00:25:26 The previous survey was docs-wide, and I think… For, robust analysis, it helps to rerun the same questions, so that we can compare Survey over survey.
But I do think that we could potentially add a few questions based on the advancements and, like, Jay's work with the Ecosystem Explorer, like, if that… takes on some kind of presence in the docs more than, you know, like, the collector, updates as it is now. Like, there are a lot of changes in the works that I would… and I know that's probably always the case, which is why I'm okay doing this now if people want to, but… I do feel like there are, some big changes coming, so…
Sophia Solomon 00:26:17 Yeah. Maybe after the big changes, then. Like, maybe later this year, like, a two-year difference between the last survey and this one would be nice.
Patrice CNCF 00:26:26 That feels right to me, a two-year scale, and I totally agree about getting in those two major milestones, milestone changes first.
Tiffany Hrabusa 00:26:38 Okay, then we don't need to do anything. I've kind of already told Andrage, but I did tell him that I would bring it to the group, so I'll just confirm with him that we're gonna… we're gonna wait, and we'll let them know when we're ready to do that again.
The next one is also mine. I attended the first… meeting of the Hotel Blueprints project, which occurred in the end-user SIG meeting, but they're now, instead of a bi-weekly, cadence for the end user SIG, they're going to weekly, and they're rotating. So one week will just be end user SIG topics, and the second week will be hotel blueprints.
the… One of the initial things they need to accomplish is figuring out where the first blueprint is going to be published in the website. And, there are… there is a proposed architecture, which I linked, which is a top-level page called Guidance and Architecture.
That sounds fine to me. I don't really know, if anyone has thoughts about Changing that, or if there are, preferences for where in the… in the top-level nav it should go. So, please chime in.
Patrice CNCF 00:28:01 What's the timeline for it appearing?
Tiffany Hrabusa 00:28:04 They're… they're trying to do the first one pretty quickly. They want to… I don't have a specific time frame, but I know that The idea is… okay, so… workflow-wise, the first thing they're doing is creating templates. They're gonna create a template for a blueprint, and a template for a reference architecture.
And those templates are going to live in the end user SIG, and the idea is that the end user SIG will vet these, Submissions as they come in.
Once they determine that they're a good fit, that they are a good idea to, publish, then they will put up a PR to the hotel.io repo to publish them there.
So we won't have to be in charge of, gatekeeping, the blueprints and architectures that come through.
Once they come to us, they will have already, had some kind of oversight and approval.
But… The idea is once those templates come up, they want to get the first one published pretty quickly, so that, they can kind of gain traction and have an example for people to refer to.
But to do that, they need to know where it's gonna go, so…
Patrice CNCF 00:29:17 I'm okay with what Danielle has proposed, which is a top-level section, and as we've done in the past, if ever we feel it's not the best place, we can always Move it around and set up.
redirects, but as… as a first… spot for it to land, that… that's okay with me. I mean, we have a kind of a lot of… first-level things under docs, but…
Tiffany Hrabusa 00:29:49 Yes.
it's tricky. This is how… this is how you get the sprawl, right? It's like, well, it fits as a top-level thing, so let's just add it. And then, pretty soon, you have 30 top-level headings, so… There could be, like, I don't know if, like, the… If there's some way to incorporate the demo or getting started guides into this information, if… we could maybe create a top-level heading that incorporates all of those.
Severin Neumann 00:30:28 I mean, maybe more migration could be something we could also incorporate into that, like… If we do a best practices section or something like that?
a practice.
Patrice CNCF 00:30:38 So to be that…
Severin Neumann 00:30:39 Aurora.
Patrice CNCF 00:30:40 That could be, and that's an exercise in information architecture re… reorg, which… I would… delay that. Do that later.
if we all feel comfortable enough with adding in a new top-level section, which I think is okay. And I would prefer having it there, and let's just feel it for a little while, and see… get some feedback, and as we've done before, we can always Change the information architecture, the doc structure with redirects.
Tiffany Hrabusa 00:31:17 Okay, I agree. Does anyone have a preference on where it lands in the nav?
Patrice CNCF 00:31:24 So it's going to be right under docs, right? That's what the issue says, correct?
Tiffany Hrabusa 00:31:28 It'll be under docs, but, like, where…
Patrice CNCF 00:31:31 Oh, oh, in the order?
That's… That's.
Severin Neumann 00:31:36 I would put it between collector and migration, from, like.
Patrice CNCF 00:31:40 That makes sense to me.
Severin Neumann 00:31:41 Yeah.
Tiffany Hrabusa 00:31:42 Okay. Okay.
Marylia Gutierrez 00:31:44 Well, I was looking, because we do have, like, demo, and on demo it has, like, architecture and stuff.
It is, if we are, like, some guidance, isn't kind of, like, the same lines of demo, or we should change demo to be lower?
Patrice CNCF 00:32:01 Demo is already highlighted on the home page, so indeed, it could be pushed lower, but Maybe we can consider that later, and separately, in terms of how to… how to move things around.
Tiffany Hrabusa 00:32:20 Yeah, I think we can sit with it, like you said. I'm… I think…
Patrice CNCF 00:32:24 Let's try it out a little while.
Tiffany Hrabusa 00:32:25 Yeah, the best information architecture decisions are going to come from seeing how things fit together and how people are using them. So I'm fine, top-level page between collector and migration, and then, we can revisit this, I don't know, in several months, and see.
Hopefully we'll have some blueprints soon, so…
Patrice CNCF 00:32:48 If we need to, and things feel a bit too unwieldy at the doc's top level, then on the doc's landing page, maybe we can have, like, a navigation map for people to figure out… I'm laughing, but I'm serious, in terms of what is where, and what sort of information Yeah.
Tiffany Hrabusa 00:33:12 Okay.
Sounds good.
Patrice CNCF 00:33:14 But again, that's later.
Tiffany Hrabusa 00:33:16 Later.
Okay, so, just keep an eye out for the first OTEL Blueprints PRs. Hopefully, they'll be coming soon, and I've… signed on as the docs liaison, so, I can take point on copy editing those, but, If anybody else wants to jump in, I'm… more than willing to have the help, so, yeah, okay, Diana and… Oh, sorry, did someone have something else to mention there?
Patrice CNCF 00:33:48 No, sorry, I just said thank you for… oh.
Sophia Solomon 00:33:51 Yeah, and I'm also in the end user seg, Tiffany. I couldn't make the last meeting because I hurt my butt, but, I'm also in the end user seg, if you need anything.
Tiffany Hrabusa 00:34:01 Okay, great. Thank you, Sophia.
Severin Neumann 00:34:03 Is there… is there any needs, like… I think the only question I have, like, additional to the blueprints, I'm just thinking about it, like, is there any need, or what would they need from our side also for, like… I would assume there's some… some architecture diagram or something like that? Have they already figured out how they do that?
Tiffany Hrabusa 00:34:26 They haven't gotten there yet.
Severin Neumann 00:34:27 Yeah, yeah.
Because if they do mermaid, or if they do sembishils, like, I mean, we talked about this at some point already.
So, yeah, maybe we can…
Tiffany Hrabusa 00:34:40 I'll… I'll bring that up in the next meeting, just to see if anyone's thought about it. Thank you.
Vitor Vasconcellos 00:34:52 Okay, so, moving to the next item.
Deanna mentioned the… Regarding the localization projects. So, I think there are two… Two items we could… We could bring here, which… the first one is to improve the visibility and observability to… So, the localization projects, and I also just added another The link to the… Looker Studio, the public dashboard from I think it's Google Analytics data we have here. If… is there any way to include the localization, I think? And… Well, there's… The other item we… regarding the… gathering feedback from general public, and, well, Deanna, it's… if you're… Have some extra ideas to share with us?
Diana Todea 00:35:51 Yeah, yeah, thank you, Victor. I mean, thank you for the blog post. I think it was, no, Marilla, I knew, Victor, who published this, and I think it was really great because we… came with some data that wasn't, made public yet, you know, at least for localization, so all of a sudden, it was really great to see all this, explained, and for people to understand. And also in terms of, you know, how much contributions have been done, to which, languages, etc. So, what I've been getting from the community, just talking at different events and so on, is that people need a lot more observability and a lot more insights into how we are measuring open telemetry. Not only localization, but in general. So… I recently had somebody coming in asking me, okay, so how do you measure exactly how many contributors do you have per whatever, you know? So, you can expand that to all six. So, like, what observability do you have?
How do… whatever. So, do we keep track of this? How do we keep track of it? Is it made public? Is it, you know, stored somewhere? So, I think maybe it's a good idea Yeah, well, dev sets. But, more like… I don't know, maybe we can make it more detailed, or more specific.
For, you know, SIGs and so on. So I think, anyway, when I saw Victorian, anyway, Marlia's blog post, I think it was really great that it was some… some introduction into that.
And secondly, yeah, what's the feedback? Do we get any feedback from external users, like, not necessarily contributors? I know we get, like, for each PR, when they contribute, there's, like, people that don't contribute, do we get somewhere, like, do we store somewhere this… this feedback?
Patrice CNCF 00:37:54 To answer the question about the Looker dashboard, it's very, very flexible, and we have access to that, and we can add statistics. I'm not sure what kind, you would, might want to see there. In terms of improving visibility and, and, and, offering insights.
We are kind of doing that with the year in review, so I think if you're comfortable with having a once-a-year snapshot.
of where we stand, then I would… probably prefer that as an approach. We… we can add… if we need to mention, you know, different SIGs and get data relative to different SIGs, we can certainly do that, but I would probably push for… I think it's once a year is enough.
Than having to, That's my… my perspective. Rather than having to… well, I mean, we can narrow the window, but we should do it at certain milestones in the year, which could be once a year, and publish a report.
How does that sound?
Diana Todea 00:39:15 Well, from my side, it's okay. I think, I mean, it would be nice to a bit brainstorm this even further, because, I mean, I know the generic idea is out there. I don't think we should put more workload at this point to generate more data, you know, periodically for… Something that we don't need. But the idea is that if we want to get some insights or some observability, maybe we can discuss it, like, in generic terms. What do we want to achieve?
what'll be good for us, you know, and think about it, first, without, you know, actually going to the concrete steps, but think about, okay, what do we actually need here? Is it useful for us? Is it… I don't know.
something we can… we can, benefit from. I don't know, let's see. To be honest, I… I, thank you for linking me the Looker stuff. I… I didn't know it was there, so I'm gonna take a look at it, for sure.
Marylia Gutierrez 00:40:15 Yeah, I think my question would be, like, what is the goal of this question? Like, people are coming to you asking, like, oh, I want to know this, like.
Okay, what… what do you need to know? Like, what is there that doesn't… like, from the links that we shared there, there already exists, what is missing there, and what is your goal with that? Because it's just like, oh, I want to see which number I'm in, like, yeah, we're gonna…
Diana Todea 00:40:37 Yeah, no, it was…
Marylia Gutierrez 00:40:38 But then we're not gonna create, like, special, like, surveys or stuff for that, but… service note.
Diana Todea 00:40:43 Yeah.
Marylia Gutierrez 00:40:44 parts, but…
Diana Todea 00:40:45 I received, like, one… I mean, not weird question, but it was, like, interesting, unique. It was like, for example, how do you know, I mean, how many, contributors do you get, and how do you know if they continue to contribute?
So, like, do we keep, like, I don't know, a track of contributors for each SIG or something, or how do we know that they keep contributing? It's like… I think that we don't have that type of insight, right? So, unless, like you well said, everyone, every contributor knows, you know, they go to… with their GitHub, whatever name, and they check their own contribution dev stats, and so on, but it's impossible to come up, right, with figures like, oh, OpenTelemetry had this amount of contributors, or… I mean, at least I've seen from localization that we do have such a score.
Based on the blog post, So, I'm not sure if we keep track for other SIGs or not.
Yeah, anyway, that was a unique question, maybe.
Victor, I don't know how you guys pull the data. I mean, you said something with GitHub Actions, etc, but… I mean, is it worth doing that in the first place, to come up with a… say, like, oh, yeah, all the saves came up with this amount of contributors per year, and… I don't know.
for what? Showing off that we have an adoption of contributors? Maybe that was the question, I think, that was coming from the general audience.
Patrice CNCF 00:42:23 Maybe we could revisit this, When we create our next year in review, and then decide which stats we want.
When we worked on the year in review, I think all of us working… contributing towards it are aware that we need to balance how much time we spend In gathering data, which statistics we want to get.
So we had that conversation in December.
Because, as I've mentioned, I think it's… interesting statistics for people to have, but they'll spend, like, a minute on it, and say, oh yeah, that's interesting, this SIG, this, that, and then move on. So, it's… it's worth doing, but we need to balance how much effort and how many day… how much, statistics we get, that would be. So, I would say, let's… reconvene in December when we talk about the next year in review, and we can.
Diana Todea 00:43:22 discuss statistics, STEM, and… yeah.
Perfect, thank you, yup.
Tiffany Hrabusa 00:43:29 I just had a quick question, and I don't want to extend the conversation too much, but… this feels like it should be a solved problem. Like, isn't there probably some, like, GitHub action or something that would keep track of, like, new contributors to a repo, and how many contributions they've made to a repo, and something that we could automate, basically, so that we can just kind of pull that data?
I feel like with open source, being.
Severin Neumann 00:43:57 Yeah, somebody must have… My last job, we had such a GitHub action, I can… I can see if I can find it. So what it does, like, it creates a markdown file, I think, on a… like, you can configure it, and then it tells, like, who has done how many contributions, and how many of them are new contributors. But that's maybe not a comms problem, that's maybe something, like, we could solve for the whole project, so…
Tiffany Hrabusa 00:44:20 Right. Yeah, that's what I was thinking. We don't have to go into it now, but it just…
Diana Todea 00:44:25 I mean… Yeah, sorry to interrupt, but why I thought it was a unique question and interesting, also, like, seeing this blog post where you announce for localization, it would be nice just to do it for the entire OpenSelemetry projects, because I… I felt like when I got asked this question, it was, like, something like, oh, we want you to show us some data about, you know, how many contributors there are, like, for what, I don't know, whatever, SIGs, or, you know, we can narrow it down and maybe show it to the public, okay, so… this, how much contributed, and, you know, this panned out, I don't know, depending on how we manipulate, or what we want to get from the scripts. But it was interesting to understand, you know, maybe, like, the, Also, how many new contributors do we have, and then how many of them are dropping? Because what I did explain to this person, for example, is that there is… I mean, at this point, we don't know how many will be still contributing, or they will be dropping.
And keep… keep going in motivating the users. It's like, it's really impossible to keep motivating, you know, contributors to keep going, and… yeah, anyway, I think a blog post or something like this would be maybe interesting to publish once a year, or, you know, something like that.
Patrice CNCF 00:45:46 Again, I support that idea of a blog post, but maybe to tie in with what, Tiffany, you were suggesting, and yes, the stats are there, I was going to suggest to Fabrizio that towards the end of the new homepage, some other sites, what they do is they actually publish live stats Relative to number of stars, number of… so we could add… we could make that part of our process where we update these stats regularly on the homepage, and kind of brag about how many stars and new contributors we have. I'm not sure we want to deep dive into how many stick around, because There's not much word… Well, we could look into that, but, it might be deeper.
More effort to get those sorts of answers.
Fabrizio Ferri Benedetti 00:46:35 Yeah, we can definitely do that, and like, currently, in the new homepage, we have one dynamic status, updated on build, using our YAML files, which I think is the… a number of integrations, if I'm not mistaken. So that's… yeah, that's certainly a way we could, we could go forward. We just need to agree on what to show, I guess.
Patrice CNCF 00:46:57 Yep.
Diana Todea 00:47:00 Thank you, guys. I need to drop, but it was, I'm gonna show up more in the next meetings at some point. Thank you so much.
Vitor Vasconcellos 00:47:11 Incope.
Patrice CNCF 00:47:16 Jay is next.
Jay DeLuca 00:47:18 Alright, so… yeah, I'm here on, behalf of something me and Jack have been looking at, so… There is the, for people who may or may not know, we have this OpenTelemetry configuration repo.
Where a lot of the schema for OpenTelemetry is handled.
And, Jack has created some, automation that generates some Markdown files for a lot of the documentation associated with it, particularly these two pages, Language Support Status and Schema Docs.
And, so this is all already, automated, generated, but as you can see, it's… It's a lot of information, it's very dense, and it can be kind of challenging, like, this is just the C++, and then there's one for each language, which basically maps each type and their support status, and then the schema has the, all the available options and things like that. And so… we wanted to get this out of the Markdown, and get it into the OpenTelemetry site, in a way that is a little bit more discoverable, and then potentially experiment with different ways to show the information so you can you know, navigate. And so, I've put together a, kind of a proof of concept, but I did it in a little… I haven't seen this approach used in the repo, and I don't know if it's a great idea, but essentially, like, for some of these things, it felt like if we could use JavaScript to make them a little bit more dynamic, it would be a better user experience. So what I did was I put together a workflow where it basically generates the markdown files, and so, like, this information is still maintained.
Like you would see it.
If it was just a table.
And then what I do… so I have that, so this is all completely automated, so, like, changes happen in the other repo, it updates these markdowns, and then what happens is… again, I don't know if this is the best way to do this, but I have some JavaScript that basically pulls that markdown table.
creates, like, an object with the information, and then generates some additional DOM elements and some… some event listeners for, like, the searches and things like that, and it gives us, you know, a different way to present it, and you can, you know, filter and search and do all that. And so, this feels like a better way to display the information, but again, I don't know if it's the best way in terms of… like, one of the things that Jack and I were talking about was… it feels a little weird to, like, convert something from, like, the schema into Markdown, and then the Markdown into, like, a JavaScript object, and then back into… something else, so… I might try and experiment with that. I had thought, like, oh, maybe we could turn these into, like, registry entries, and then pull the information that way, but that felt… a little tricky with the existing registry schemas, things like that. But all that to say is, like, I wanted to… and then we have the types as well. This one's a little less dynamic, but one of the things that I did do was apply some styles to… Like, set max widths on some of the columns, and do some other things to try and at least make it a little bit more, fit a little bit better on the pages.
Yeah, so I'll pause there. Oh, one other thing is, I still need to put some thought into how something like this will work with localization efforts, because that's obviously really important, and we need to make sure that there's a fluid way for us to handle, even if it's just, like, the headings and the search bars and things like that. But that's certainly on my radar. But yeah, I'll pause there.
I see, Raise their hand first.
Jack or Patrice, but…
Jack Berg 00:51:16 Patrice.
Patrice CNCF 00:51:17 Jack, did you want to go first?
Jack Berg 00:51:21 I guess I was just going to add a little bit of color. I think Jay has done an awesome job here, and did a really good introduction to this. Just a couple of clarifying points. This is for declarative configuration. You know, it's the… alternative configuration scheme that's been in development for a couple of years, and it's just about to stabilize. We're going to stabilize it on the spec soon, and it aims to solve a bunch of the problems with usability and expressiveness that come with environment variable configuration.
And as we move from sort of, like, this is in development to this is stable, we want to push this, you know, to users more. This is going to be part of, like, an improved user experience for people picking up OpenTelemetry, because they have this richer toolkit that allows them to configure how their SDKs and instrumentation behave without them having to, you know, write code to integrate it.
So, this is, I think the… some of the first surface area on Opentelemetry.io where we're trying to surface this, like, declarative config stuff, and And, you know, we kind of need to put our heads together. We have a lot of content, as Jay has shown, there's a ton of information. We need to give some special thought on, like, you know, how to display it to, you know, keep it navigable, to keep the information density high, and to, like, guide users to the right information as quickly as possible, so… I'll stop there.
Patrice CNCF 00:52:51 I think this is great.
And the way you've set it up.
I believe makes sense and works well, including the generation of the markdown.
The interface looks wonderful. I've been trying to work towards, figuring out… how to… Structure things more in terms of components.
For the web, for the website, but… I won't get to it for a while, so I would run with this.
I think having the markdown file is nice because it makes it discoverable for SEO and AI, and having the web interface for our users makes for a beautiful user experience, at least in terms of what you've shown. So I would… I… fully endorse.
this.
I don't know how… and maybe we don't need to worry about it, but we've had issues with the registry. I've had issues with the registry where it, just seems to take forever to load, and… become usable for the user. If we could avoid that, if there's a lot of data, and it's probably just having appropriate programming, but, that would be the only thing I would want to avoid, to have long delays for our users, but otherwise, I think this is fantastic.
Thanks for… thank you both for, working on this.
Jay DeLuca 00:54:31 Rulia?
Marylia Gutierrez 00:54:32 Yeah, so, well, just sharing here, because me and Jay already talked about this, because, yeah, he showed me this before, I also agree, looks great. So yeah, just sharing, like, the concern that I brought to him, that he put it here, was regarding, like, the localization, because it was… If we create this always dynamic, or, like, maybe on the fly or whatever, localization team would never know there was a change, and needed that, so that is just something, like, to consider, like, we can have, like.
a script that could be, always reads and, like, publish, I don't know, create, like, a new PR, and on this one, it would have, like, a new hash, so the localization team will know that this had some changes, because a lot of the things is, like.
The name of the parameter, those things we don't usually translate, but the meaning of the thing, we do translate.
So, it needs to have, like, somebody to take a look and things like that. So, it doesn't… I don't think it has to be, like, can be fully automated, just because we need the localization. But as long as we had, like, a hash associated with a change, then the localization team can come in.
Jay DeLuca 00:55:43 That's a good point, so it… Yeah, so it wouldn't just be enough to be able to maybe mark something as drift if… Content itself changed, but we need to be able to identify the localizational components, and only Identify them as drift if, like, those parts change, essentially.
Cool. Yeah, I can, I'll put some thought into how we can do that.
Patrice CNCF 00:56:11 Fabrizio, do you mind if I comment about that before…
Fabrizio Ferri Benedetti 00:56:14 Sure, sure, go ahead.
Patrice CNCF 00:56:16 Okay, in terms of localization, I did want to mention, that We've chosen, for example, for the registry at the moment, to not make it something that is localized. We could… At least temporarily, for this initial spin, decide not to localize.
this work. If we do, we need to decide which is more important for the end users. Is it to get an English version that is Cutting edge and always up-to-date, or… If things are gonna drift.
depending on how quickly is it worth having a localized version, but that is very far behind, how useful will that be? And then there's the problem of figuring out how do we manage translations, and would it be just a, Jay, do you think we could handle it just as a drift over the Markdown page that contains all the information?
Jay DeLuca 00:57:18 Yeah.
I mean, that's the original thought, but, like.
That comes down to, like, there will be… you know, the… because, yeah, the markdown pages is what I would use to detect the drift.
But… We would only want to care about certain… parts of it, right? Like… If a property name changes, we don't necessarily.
Patrice CNCF 00:57:44 Oh, we do want, so I would track any change in that file. It's just, I see it as a file that will probably change often, and so drifting will happen quickly.
And then the… what we need to decide is… As I mentioned.
In terms of user experience, if… what do we want to offer, people Users of other locales, whether something has drifted a lot.
in rendering, or just the English page?
Marylia Gutierrez 00:58:18 Will it change often?
Patrice CNCF 00:58:21 That's a good question.
Marylia Gutierrez 00:58:23 I don't think… because, okay, right now we are stabilizing, so I might have, like, things now, but after that, I don't see it changing a lot. I might have, like, things here and there, but yeah.
Patrice CNCF 00:58:33 Then good, then why not handle it the way we handle any other age?
Do you see that as working, Marilla?
Marylia Gutierrez 00:58:44 Yeah.
Patrice CNCF 00:58:45 Okay.
Marylia Gutierrez 00:58:47 Yeah, for Bizzou?
Fabrizio Ferri Benedetti 00:58:49 Oh, yeah, just, just, well, first of all, I agree with the, analyzing the localization, and I also find this work to be fantastic.
Just one thought about, especially about the language status and similar content we want to push forward is, one of the things as an OpenTelemetry user and contributor I miss the most is, like, something that I can go and very quickly find out what the status is of, say, specs, features, etc. So, I wonder if we… and, you know, like, right now, it's, like, kind of buried.
I think that given our status as incubating project, it would be nice to think about also putting these, like, nearer to the user, maybe as a first-level item in the nav, like status, for example.
Where, you know, you can go and check the status of specs, language features, everything, and it's like, is it ready yet, right? Like, for example, are… is profiling ready yet? And currently, to answer this, you have to click quite a bit on the docs website.
And, I think it would be nice to… think about, like, this kind of status hub where we say, yeah, this is still cooking, you can go there, this is ready, etc. Any thought on this?
And also to showcase, like, the fantastic UI that Jay has been working on.
Patrice CNCF 01:00:18 But we have the status page, right?
The status page should, in principle, be the place to go to get that sort of information, though we might link to what JS?
Fabrizio Ferri Benedetti 01:00:31 Yeah. Is that what you had in mind? Yeah, yeah, we could, like, give a, like, use a status page maybe to give a little more visibility, or even… like… yeah, like, even this… this table could be… could use, like, a little more love, like, similar to what Jay has done with the language status, I don't know. You know, something visual with… I really like the semaphore thing, you know, with red, yellow, green, think we could have something like this, too, here.
Jack Berg 01:01:03 It's like trying to model every, Every entry in the docs, whether it's, like, pages or sections in pages, as components, where each component has its own, you know, status.
Fabrizio Ferri Benedetti 01:01:16 Yeah. And…
Jack Berg 01:01:17 That seems like a kind of a big undertaking,
Fabrizio Ferri Benedetti 01:01:20 Yeah, yeah, yeah.
Jack Berg 01:01:21 Not all the topics you talk about have status, but many, many do, right? As someone who wrote, like, the OpenTelemetry Java docs, it's like, you know, basically every header in that is a component which corresponds to a section of the specification. So all of those have a status associated with them, but not all pages are like that.
Fabrizio Ferri Benedetti 01:01:39 Yep.
Jay DeLuca 01:01:46 Any other thoughts on this one?
Jack Berg 01:01:49 I left a comment on the PR. I think we need to give some thought to the, like, the information architecture, just the title of pages and how the navigation hierarchy is arranged here to make it clear a couple of things, like, you know, this is… the top-level section here is SDK config, so we're talking about configuration of SDKs. Well, there's a couple of different main paths you use to configure SDKs. There's programmatic, there's environment variables, and declarative config.
And, You know, the pages that you've added here are only related to declarative config, and the titles of the page and their position in the hierarchy doesn't necessarily suggest that.
So we could nest these new pages under the declarative config page, but, you know, is that too many levels of the hierarchy?
So we… we just need to give some thought about how to present this information to make it clear, you know, what you're actually looking at the status of, what these types are actually describing, their, you know, their types within the declarative config.
world.
Patrice CNCF 01:02:50 Just a comment about nesting, we have a means of routing a section now in the website, so that we don't have to worry about nesting. You can nest to your heart's content, and we can root, for example, the navigation section for just config.
And that way, you kind of get a new root and don't need to worry about the nesting.
FYI.
Jay DeLuca 01:03:20 Cool, so what I'm gonna do is, there's still a couple other tweaks I'm gonna make to it, so I'll go… so now that I… I think that there's consensus that this is, an appropriate work… workaround or approach, yeah, so I'll polish it up, I'll address some of this stuff, and, yeah, I'll try and get it into a position where we can look at it again, and… Hopefully get it in a good shape before we get to the stability push.
So, thanks everybody.
Severin Neumann 01:03:48 I know we're at time, so we don't need to go too far into this, but…
Jay DeLuca 01:03:52 Yeah, Ecosystem Explorer Project, I'm… I talked to Severin about this yesterday. I'm gonna start putting in the steps to get a repo created, and then we can create, like, an approvers group and all that, and start… actually building the thing. If anybody's interested, I do have… I have been making some notes, I have some things that I want to discuss further, we can do it async, and I put together, kind of, a high-level, phases of, of, like, I think of the work that needs to be done. Certainly subject to change, but… Yeah, now that we're in the new year, I want to start actually moving forward on this, and I'm still… I've still been working on my forks and my proof of concepts, but now I want to get it into the… OpenTelemetry org and all that, so… I will stop there.
Patrice CNCF 01:04:42 Great, thanks.
Jay DeLuca 01:04:44 Thanks, everybody. See ya.
Severin Neumann 01:04:48 Thank you all, bye-bye.
Leandro Caracciolo 01:04:51 Bye, thanks.
