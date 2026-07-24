SIG: Go Compile Time Instrumentation SIG
Date: 2026-07-23
Duration: 69 minutes
============================================================

## Zoom Recording Transcript

Kemal Akkoyun 00:08:35 Hello, hello.
Dario Castañé 00:08:44 Hello.
Azhar Momin 00:08:45 Hello?
Kemal Akkoyun 00:08:47 Good morning.
I see you haven't started yet.
Dario Castañé 00:08:53 We were waiting for you.
Kemal Akkoyun 00:08:55 Oh, thank you.
Do we have any agenda items?
I can go ready to check.
Let's chat… Okay, this is a new meeting.
It's shared… Boom.
Okay, we have… Usual suspects here.
And I should… yeah, feel free to add your names as attendees.
Okay, this is not wrong.
I have too many meeting notes.
Which one is this?
Okay.
Interesting.
Azhar is here, Dario is here… I'm giving people time to… If they have any agenda items to just add them.
Okay, So, my agenda item is we want to do some issue triaging together.
Okay, Jan is here, nice.
So, we want to do some issue triaging together, and have a look at them.
And… Maybe, no.
We don't need to discuss this, but, like, I would like to bring the RFC again. We have a lot of discussions On… slide.
So feel free to contribute.
and review the RFC. This is… this is important.
This is kind of a major step for the tool, so, like, Please check it out.
add more comments, help Azhar to, like, polish the RFC, because we also need to start implementation, implementing it, I guess, this week, because we would like to ship that before the LFX, term queue.
Are we in Q3? Q3, I think this is the term 3.
Before the term Qi ends.
So that's… that's the first thing.
Azar, do you have anything else to say about it? Do you need any specific, comments?
I thought Azhar was in, no?
Dario Castañé 00:12:25 And she's having some issues with the setup.
Okay. He will be back in a second.
Kemal Akkoyun 00:12:38 Cool.
Okay, before the issue triaging phase.
We have… A lot of new faces.
If you wanna, like, say hi?
Feel free.
Don't feel the pressure, but, like, it could also help.
Mohamed Kamal 00:13:04 Hello?
Atharva Mhaske 00:13:05 Okay, sorry.
Kemal Akkoyun 00:13:08 Now, we have a race condition. So, yeah, like, we can use the race hands and, like, Alright, Atharva? Maybe you should go first, I saw your name first. I don't know if I'm pronouncing it correctly.
Atharva Mhaske 00:13:22 Yeah, it's right.
So, hello guys, myself, Atharva. So, I'm currently in my final year of undergraduate.
I… I work as an open source contributor in OpenEverest, which is CNCF sandbox project. I there manage LLM inferencing.
provider SDK, where we work on deploying LLMs with the help of CNCF, KSERP, and VLLM.
Also, I have been working with Golang over a year now. Like, I have built many tiny projects and did a few internships where the Major League stack were in Golang. And also, I'm looking forward to contribute in a wide variety of CNCF projects. I am right now.
like, looking forward to contributing this Compile Instrumentation repo as well. So that's all.
Kemal Akkoyun 00:14:25 Alright.
Atharva Mhaske 00:14:26 Yeah.
Kemal Akkoyun 00:14:28 Okay, just a point of order.
There is another Zoom link, is it?
Because, like, I've been… He's in another Zoom meeting.
Dario Castañé 00:14:46 This is the updated one, I make sure…
Kemal Akkoyun 00:14:49 This is the updated one, right?
Dario Castañé 00:14:51 Yeah.
Kemal Akkoyun 00:14:51 Because they, like, they put their name…
Dario Castañé 00:14:53 error.
I went to my calendar to compare the different… slots I had for this meeting, and this was the one that had the right one.
Kemal Akkoyun 00:15:03 Okay, we are in the updated one, right? That's the correct one.
I'm just writing.
And should we update this link, then?
This is the correct one, right?
Dario Castañé 00:15:39 Yep.
Kemal Akkoyun 00:15:41 Okay.
And we already have the correct… or maybe… did you update this one?
Dario Castañé 00:15:49 Hmm, nope?
Kemal Akkoyun 00:15:50 No, I did, I'm not sure.
Let's check if they match.
Yeah, very much. Someone updated it.
I hope.
Okay, mmm… I just want to make sure… yeah, that's… that's the correct one.
An updated one. Cool.
Thanks for the introduction.
Mohamed, do you want to go?
Mohamed Kamal 00:16:28 Yeah, sure. My name is Mohamed Al Kamal, I'm a senior computer science student at Cannel University in Egypt.
And I also love doing, open source, I think it's a… it's a great thing, like.
get mentored in the current job market. So yeah, nothing crazy going on here.
Kemal Akkoyun 00:16:52 Awesome.
Welcome to the community.
Okay.
Alright, so… what do we need to do? Azhar is not here, but yeah, let's check the RFC, and then let's then jump into… some issue triaging, that's what I would like to do, mark some of the issues that are already good first issues, so people can have a chance to, like, start helping. Also, maybe we can Judge… Any… yeah, if any bugs that needs, like, special attention.
I think someone from the commenter already Did a good job on, like, marking some of these issues.
That could be a good first issue. Let's start with that.
And this is what we already done.
Great.
Cool. So we need… Like, yeah, we checked this, that one, we already know this is… The proposal for Term 3. We have two LFX projects for the next term.
Sorry, next term is term 3. Are we in term 2 now?
Confusing.
Okay.
So, yes, let's check this one… This is another… And the fixed project… How they're wrong.
Wow, too many new issues.
Yeah, we returned to… And the rest is the old ones.
I don't know if we have any good first issues with this.
Can you check the old ones… I need to tackle these.
We are already something for this, I think.
Those legs are already working on this.
Okay.
So this idea of as a foreigner.
Jesus.
Something like… Not a low one, but, like, a truly moderate one, so we need to add a little labels now.
You don't have… I have to moderate interest.
One thing yellow.
I never understand how they update this one.
Yes.
But it's already there. If you have any comments, just feel free to, comment on these things. So this is also… And effects… Turn 3?
I think… This is a high effort one.
So… We will have an MNT for working on this.
Lord… What is this? Hmm… I wouldn't say, like, a bug. This is a first issue and a feature.
that we miss… Dario, I remember you worked on similar stuff, but I… maybe we didn't finish this implementation.
Yeah.
has directed as exit.
Dario Castañé 00:22:29 I did something, yeah.
Kemal Akkoyun 00:22:34 Yeah.
Dario Castañé 00:22:36 There is…
Kemal Akkoyun 00:22:37 This is acute.
Dario Castañé 00:22:38 from what I see…
Kemal Akkoyun 00:22:44 Okay, so… We can already assign this to…
Dario Castañé 00:22:50 Yeah, let's assign it.
Kemal Akkoyun 00:22:58 Boom.
So, adding more unit tests.
Yeah, good first issue, and already I think there's a TR.
Okay.
What's so sorry.
Cool.
People are opening issues and fixing them. Amazing.
The wrap size calls pest rule is missing the pet fields.
Yes.
This is a beer.
Azhar Momin 00:23:40 This one. This one is, I think, already resolved, so… close it, but I think we can close it for now.
And it can be reopened, if there is something missing.
Kemal Akkoyun 00:23:53 So there is a… this is already fixed?
Azhar Momin 00:23:56 Yeah, this was already… yeah, yeah.
Kemal Akkoyun 00:23:59 Okay.
Allow applications to use auto-instrumentation manual at the same time, yeah, okay, yes.
Hmm.
Yeah, this setting it once may help.
But, yeah, this is a nice use case. I don't know how we can actually manage this.
But we talk about this with Azhar when we were wiring the providers first. Maybe we should, like, check if it's already assigned and whatnot.
Azhar Momin 00:25:00 Right? They can already actually, disable this by pinning, but we currently don't… allow them to come at the generated hotel Instrumentation goal. Also, I think we have a hook which skips all the feature calls to set global provider. I'm not sure why that's there, I'll… try to ask Hybean about it, since he wrote that part. I'll confirm with him, and maybe we can remove it, and then they can override the default one.
Kemal Akkoyun 00:25:34 Okay.
I'm gonna assign this to you, and maybe… you can propose some other solution. Rather than you fixing it, just investigate and add a comment.
And we can let someone else to solve it.
I mean, this would be… I don't know if it's a bug?
Question, do we have a question label?
Not yet.
I'm not sure about that.
Let's… that's wait. Hold on about this.
Single filters, fatal functions with the slice channel map endpoints instead of no match.
Yeah, we shouldn't crash, for sure.
I mean, if it's a valid thing, we are okay to… have a PR on these.
So, yeah, for everyone, even the room. Yeah, I mean, if it's, like, enough reproducible, and if you have a clear case, and it's bug, and if it's blocking anything, feel free to send the PR patch. You don't need to, like, discuss anything in further, but if it's, like, a design decision, if it's a big change.
If it's, like, some sort of… if it creates some sort of controversy, we should definitely hold on and wait for wait for any implementation.
So for more complicated demos, what I mean is, like, we have… okay, we have HTTP tests, but we don't have, like, a… layered applications, as I, like, mentioned there, which is, like, more real-life scenarios, and especially for, like, distributed tracing, which is, like, more relevant, right? You have a trace? Okay.
it got an HTTP request, it's doing a SQL request, maybe making a Kafka streaming call. We have all these, like, default instrumentation, but I realize, like, we haven't actually, like, testing those, because especially this… Came to mind after.
I think… recently… Xavier created, yeah. So, for example, he… Or get to enable auto propagators.
And, like, this would have been cold.
with certain, like, tests, right? I would like to eliminate the cases like that. That's why this is here.
And I will say, already, someone… Created.
And PR… Yeah, you can check, dependencies.
Yeah, that's the more complicated scenarios, like, layered applications, real-life applications, because, like, we have integrations, again, just like HTTP test demo, but it's just HTTP server requests. I've seen people, like, we have, I think.
I've seen people trying this, and see… I haven't… and they couldn't manage to… propagate the context properly for HTTP SQL combination, and we… they weren't seeing the whole demo thing.
So yeah, we need to check if it's, like, working, since Ariane is already working on this. I'm gonna assign this, And he didn't comment it.
Let's see if I'm gonna make it correctly.
Okay.
Let me get check for this later… So, injected SIG term, SIG 100 forces instead of re-raising the signal. Why we need to re-raise the signal?
Hmm.
Didn't know about this.
Yeah, maybe if you don't exit, that's true.
Okay, someone's already… Working on it… You need to review this, that's the problem. So, like, any newcomers, feel free to help with the review. You don't need to wait for a maintainer to review that. If you already know What to do, if you have any improvement suggestions.
Go ahead and review these as well.
It could help.
For maintainers to make the judgment calls easier.
Okay.
migrate HTTP metrics, all the Telemetry Kamal type builders, you know, makes sense. Yes.
Someone is already working on it. This is… fast!
Okay.
You guys are amazing. Is this happening because of LFX?
Or is this because of VA and V1? Like…
Mohamed Kamal 00:34:28 I think it's because of LFX, like, usually mentoring, programs, brings a lot of, newcomers.
Kemal Akkoyun 00:34:38 Makes sense, yes. We've seen that the first wave.
I think they just, like, coincide.
Okay, this is effort high, for sure. I'm not sure if it's a good first issue. It's definitely a group effort.
Someone is already… Something to do that.
Why… I don't know, like, Ian and Habin, they wrote their names, but I don't see them in the meeting.
Okay, they said that they're another meeting.
Aren't in the same meeting.
I'm confused.
Is this the same meeting or not?
Azhar Momin 00:36:09 It seems like the same link.
Kemal Akkoyun 00:36:12 Same link, but they are not here, right?
Azhar Momin 00:36:15 Yes.
Kemal Akkoyun 00:36:23 Interest.
You clicked that? Okay, I'm not sure.
Okay… Interesting.
Well, what happened to this? Like, we submitted two of the LFX.
Issues.
Waqar 00:37:07 Absolutely.
Okay, so, like, this is… Hey, Kamal, I am audible to you.
Kemal Akkoyun 00:37:17 Yeah, yeah, I'm hearing… I can hear you now.
Waqar 00:37:20 Okay, sorry for interruption. So, this was initially my proposal for LFX, but due to limited scope.
Xavier had dropped this, but I am in discussion with him to open, like, sub-issues from this.
in coming future. So, there are some design decisions that we have to make, so I am in contact with Zabir. So, like, in the near future, I'll open sub-issues from this thread.
Kemal Akkoyun 00:37:48 Okay, so this is, let's say, this is a high effort one, but it's not LFX, right?
Waqar 00:37:55 Yes.
Kemal Akkoyun 00:37:57 Okay.
Thank you for the clarification.
Record compile time, prop version on the Telemetry. Oh yeah, this is… we already have something.
Yes, I assigned this. It's a good one.
Yes. Yeah, that… this… yeah, we… we missed this. This actually makes sense. I don't know if… we should use the distro. I don't remember the details of the semantic conventions, but it would… at least at this point, until we submit the instrumentation from Hotel C, This is really helpful, so that we know, like, which autassi actually used.
But, like, eventually, we need to decide, like, also somehow put the instrumentation version that is injected into the label somehow.
But it's one problem at a time.
Someone is already doing it.
Hmm.
I keep repeating the same thing, but I would love to repeat for all the LFX mentees, whether if they, like, watched the recording and whatnot. I really like that you are enthusiastic and whatnot, and contributing to the project.
But it's not the only criteria that you are contributing.
And it doesn't guarantee, selection, so you computing this hard before, and then you are, like… we've seen this, right? Before the… before the previous LFX, people really swarmed on issues, they helped.
And then they just… away after the selection finishes. It's not sending the right message. I understand the motivation, but you shouldn't be just, like, that selfish about the community, whatnot. Like, try to be… contribute after maybe you aren't selected whatnot. Like, apparently you're interested in these.
So yeah, also, like, we check a lot of other criterias when we are selecting a mentee, and the contributions is not… a huge chunk of that. This shouldn't discourage you, like, showing that you have abilities to understand the problems really makes a difference.
But it's not the only criteria.
Okay, we need to review this. I think there were two, PRs on this, and… I commented one of them, and the other one is get closed, but we need to review. Again, help with the reviews, like, that's… that's also… really… That shows that another, Signal for, like, responsibility, or helping the maintainers, that you understand the context and whatnot, so… the creating an issue or, like, signing a PR is not the only way to contribute.
So… I think we already have a… Beautiful note.
You should definitely… Need a new label for instrumentations, so… So… That would be cool.
Integration, Instrumentation, you never know what to call these.
Instrumentation, okay.
Jay Sawant 00:42:25 Probably not?
Kemal Akkoyun 00:42:26 Document and define the Telemetry signal coverage for instrumentation, yes.
Can someone help, like, share this meeting's URL? There are 4 people in another Zoom meeting.
And I think…
Zhanghaibin Zhanghaibin 00:43:09 I'm back.
Kemal Akkoyun 00:43:11 H.
Okay, so we are on the same page.
I think some, like, something happened, I don't know. So, let's, let's make sure. This is the updated link, right? This Zoom meeting is the updated one.
Zhanghaibin Zhanghaibin 00:43:29 Yeah.
Kemal Akkoyun 00:43:30 We checked it a couple of steps.
How did… okay, I think that was a confusion with the other one.
Okay, so, we did a couple of triaging, Yes, this is important. Mini sort of documentation.
for the integrations, what is available, what not, maybe a table in the README, I think someone is working on it, but we also need the same thing for the available environment variables, which one we can configure whatnot for each integration. We already had discussed this on Slack.
this could be a good issue to cover. Check the Slack messages, there are some, like, ideas, like.
there will be a huge refactoring for the next LFX term for around configuration, but until that, like, people keep asking, okay, how can I disable the metrics for this integration?
How can I only enable metrics? Those sort of, like, they ask, and we have environment variables for those. I think we should document them in a way, maybe in a generated fashion from the code.
Yeah, it could be a good issue.
I didn't need to create an issue for that.
Like, that could be the first step.
Yeah, Atharva, I think you were in the discussion. Do you want to create an issue for this, for to describe this?
Azhar Momin 00:45:07 Yes, I have tried to create it.
Kemal Akkoyun 00:45:10 Okay.
No, I'm sorry for my pronunciation. I didn't mean Azhar. It's Atharva, right? That's… He was in the discussion. So, maybe Atharva can create the discussion, and we can enrich, right? Create the issue, and then we can discuss how to do this, and this could be a chunk of work.
Atharva Mhaske 00:45:29 Yeah.
Kemal Akkoyun 00:45:34 And there is also, like, Jurassi, actually proposed there is something… DOS is, I think, an AI thing, and it helps, the CNCF open source projects to generate documentation, search mode, whatnot, but I don't know about the features.
We can also, like, explore if it can help us in our project.
So… This is documentation. You don't have a documentation label?
Great.
I think we didn't do a lot of triaging before, now we discovered these things.
Azhar Momin 00:46:15 And I was also proposing having a ReadMe for all the instrumentation, so we can document what joint points we use, so it can also help with Troubleshooting and other stuff, so I'll try to create an issue for that. I was going to create for that.
Kemal Akkoyun 00:46:34 Okay, that's… that's also a good one. Please create one.
Okay… Template variables for signature contents. Yes, I think this is an actual problem that we face, while migrating our integrations. We have the signature contents, but… Yeah, okay. Hannah is already working on that. Maybe I will just assign this to Hannah.
Okay, these issues are old.
And I opened this.
Honestly, I don't remember anything about this.
Azhar commented on this, okay. Oh, you already have something to fix this.
Azhar Momin 00:47:44 Actually, this one will require a lot of, design decisions first.
Okay, I have another RFC for it, so… I'll try to…
Kemal Akkoyun 00:47:56 Okay.
They didn't realize that. Okay, assigning that to you.
Morning.
Yeah, feel free to, like, change the issue, add more context. Apparently, I didn't do a good job describing. You already have a lot of things, but you should be able to edit this.
So he won't forget about this.
Is that always unimplemented at hardcore. That's the same issue, you know?
Azhar Momin 00:48:24 And duplicate.
Kemal Akkoyun 00:48:28 So, this is 161.
Audit, pull request, target, and workflow runs for… yeah, okay, this is a good first issue.
To be honest, this doesn't require any Go knowledge, it's just GitHub action knowledge.
There is the… Yeah.
Azhar Momin 00:48:59 There was already a pull request for this. Is this still pending, or…
Kemal Akkoyun 00:49:05 It's merge? Does this cover everything?
Apparently, no?
Okay.
I think this is expired.
Oh, there was this. Okay.
Not… Okay, I think this is a… this was a big one, right? I don't know what was breaking.
Oh, you clearly want. Yeah, it's like, yeah, this is, this is the thing that I don't want.
to keep us pumping, and I don't know how to solve this.
This will be an issue for feature, for the feature, because, like, Okay… Minimum required version. Yeah, this is… this is how they, like… This is not our problem, this is client call… client goal problem, because they are, I think, upgrading the minimum required version for no good reason, and I don't know their reason, but it will be creating a lot of issues for Hotel C.
This is a huge problem, and I don't know how to actually… how are we going to solve this, and this will happen again and again.
at some point, we would like to keep OTLC supported version as broad as possible, but then the integrations will use all the new APIs.
And I think the end result shouldn't break the OTLC.
that's why I… one of the reasons that I really want to separate the hotel C from its instrumentations and integrations.
But it should… break… it will break the end user app, and it will say that, okay, if you want to use the latest instrumentation version of Client Go.
Then you need to update your, Minimum required core version.
But… I think since we also have the target range.
then Autel C can tell that, okay, like, I have… this is… there is a client Go that is version X, and I have an instrumentation range that pulls into that, and it will pull a module that is compatible with the minimum Go version, and should be fine.
I think that's, like, this is… this is the biggest… like, thing that I really want to solve with, the registry approach, or, like, separation of, Instrumentation from the tool itself, so that we don't need to keep upgrading the minimum required version of OTLC or anything, any of our binaries, so we can support a variety range of tools.
I think, Azhar, your RFC should fix this.
So… let's keep this open until the registry changes and see that if we can manage to fix this. But it's… again, it requires, like, separation of the instrumentation.
From the tool.
Here we have 10 minutes left.
Okay… Any other issues you would like to discuss? We are nearly at the end of that. Yeah, this is… Maybe this is… this also requires that separation.
Well, like, yeah.
I think this will be deprecated when we separated the instrumentations from the OTLC, but right now, what happens is, Dependabot, like, we have… we have a PR for this, like, you can actually see, yeah, where is it?
Hmm, that one, no.
But no, it wasn't this one.
We have… Very easy to do that.
And, did I close that issue?
Oh, no, this one.
Okay, anyways, what happens is… I don't know if… like, let's say that we have an instrumentation for this version, and everything is… we have the target range, but then Dependable tries to upgrade it, even though we don't support it. So… The… this idea of this was, like, somehow, keep our, like, supported… dependency ranges in a file, and make sure that Dependable is compatible with this. I don't think Dependable is, like, clever enough, but Renovate can… Actually, have, like, different, configuration knobs.
But then again, this is not, like, a big of an issue if we separate the instrumentations.
But then, this will be an issue for if we decide to create a separate repo for our instrumentations and integrations, then this will come to a place.
So… I don't know if… Anyone is, like… want to give a chance to this with CI, whatnot, this could be an interesting challenge, but again, not, like, not very high value.
Azhar Momin 00:55:12 I think this should be, fixed by the OTLC pin PR. This was, I think, before the hotel CPN PR was launched.
Which fixed a similar bug, so maybe this is already fixed. Fixed, I think.
Kemal Akkoyun 00:55:27 Okay, I, like, I am assigning this tool to validate, and maybe… Close it, okay?
Thank you.
attitudes for Jin and… we already have a PR for this, we just need to revive this.
And I remember I reviewed… Debbler review, yes.
And then I… okay.
So, this is… It's actually a good first issue, but it's already taken.
This is already… in verbs, I guess.
And I've been already checked it out, and assigning… Apparently it's part of LFX now.
Okay.
So… Did we do a good job on triaging all these issues? We assigned, we have labels, is there a filter of, like, no labels?
Okay. No labels, no assignees.
Or maybe not a Siamese?
Okay, this is… this is… And this one… Assigned to me. I need to think about this.
Who's… like, effort high, because it requires some design decisions, and I'm not sure how to tackle this.
Don't get… okay.
Okay, that can be actually a bug.
Englewood first issue, cool. And…
Zhanghaibin Zhanghaibin 00:57:31 Oh, I said to me.
Kemal Akkoyun 00:57:35 You wanna handle this? Okay.
Zhanghaibin Zhanghaibin 00:57:38 Yeah, yeah, okay.
Kemal Akkoyun 00:57:40 Yeah.
We already have a tanker.
Cool.
on, all right, all of the issues are labeled.
We have a lot of assignees.
and… Like, feel free to… Again, we already discussed create an issue and check it out, discuss with the issue owner if you wanna… if they wanna… they're open to create, like, sub-issues, if you wanna, like, contribute.
Meeting to assign this to… The color is… Right, we have 5 minutes. If, like, since Yiyan and Habin, you just, like, joined later on, do you have any discussion points you would like to… Polkobot?
To be honest, I really want your opinion on this.
I think I already put your name here.
I didn't. We should.
No, this is my company account, and I can, like… if you can… yeah, you're already, thank you.
And Yan, if you also have a time and have a look at this, This is… a major step for Hotel C, and we… I want to make sure that we are covering all the bases.
Xavier already had a lot of nice comments on this.
This is the big chunk of the LFX project that we are currently working on.
Okay.
Yi Yang 00:59:22 I will take a look when I have time.
Kemal Akkoyun 00:59:25 Thank you so much. Yes, that would be really appreciated.
Yeah, but the gist of it, we are trying to split the instrumentation lifecycle from the OTLC lifecycle by introducing a registry.
Yeah, there are a lot of details we can think about this.
And I guess, like, we started… maybe we should use the registry open.echo, like, I.O, but, like, now we are leaning against maybe we will have a dedicated repo.
Or this JSON file, or RTLC. I think Azhar has more details. Anyways, let's continue discussion on the RFC, it would be more helpful.
Yeah.
Okay.
Any last-minute comments?
Atharva Mhaske 01:00:17 So, I wanted to discuss one thing.
Kemal Akkoyun 01:00:20 Yes, please.
Atharva Mhaske 01:00:22 So, right now, as I looked into repo, for our CI, I… we don't have Go vulnerability check as we have in other Golang reports, like hotel… Go SDK or OTelGo contrib.
Kemal Akkoyun 01:00:39 Yes, go ahead for adding that.
Atharva Mhaske 01:00:42 Yeah, I was, like, about to create issue on that.
Kemal Akkoyun 01:00:48 Yeah, create, assign that to yourself. I did this work recently for… For our, like, repo.
Mmm… And I checked, so I can… Truck.
Thanks.
Sorry.
Yeah, there are a bunch of PRs, like, some of them is, like, one-to-one, can be movable here. I will drop this link.
To the meeting notes, or… For you to check, so… So go ahead. That's the message.
And create an issue, and, like, claim that, and you can check these similar issues for that.
Yeah. Oh, with that, I think we… one thing we also need to do is, especially for the instrumentations, this is the… also the part of the RFC, we need to add Cool-down period?
It is called for Dependabot.
So, like, recently, there are a lot of, like, people are… there are a lot of, like, supply chain attacks in the form of someone is, like, sneaking a PR, getting a release, it's a patch release, and then everything auto-updates, whatnot. So, too, there's a… there's this, like, idea of cool-down periods.
Which maybe say that, like, 5 days later, at least the patch needs to be, 5 days years… 5 days old, whatnot, and… like, you just don't upgrade that. Like, we can also add… check those things as well for Renovate and Dependable.
We already, like, we are not, like, opening the PandaBot upgrades, like, daily, but it… it makes, change… Yeah, this could be also the insane part for global check. This should be two separate PRs, two separate issues. The second… the latter one may require some more, like, look into in our configurations, whatnot.
Yeah, we should be super careful about this, our security stance, because basically we are changing the code, before using… noticing, user noticing, and maybe we don't even see the code, and if something happens for the injected code that we have, we can cause problems. So, anything that increase the… increase, like, strengths or security stance are welcome.
Okay, we are over time. Any last-minute thoughts?
All right, thanks everyone. I guess we'll see each other on Slack, and maybe next week.
Bye-bye.
Zhanghaibin Zhanghaibin 01:03:59 Bye.
