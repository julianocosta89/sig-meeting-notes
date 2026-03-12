SIG: CI/CD SemConv SIG
Date: 2025-08-07
Duration: 21 minutes
Zoom Recording URL: https://zoom.us/rec/share/W3sujzqK9hfkFMvDERrMyjetgYgu_rWvNiXnPtPZq0CADtaACEYfmUB9IXz5Ez6P.bgR4uHaXHsfm5DR6
============================================================

## Zoom Recording Transcript

**Dan Gomez Blanco** 01:45 Hello!
**Martin Costello** 01:47 Hi.
**Dan Gomez Blanco** 01:50 So go in.
**Martin Costello** 01:52 Not bad. Thanks. How are you?
**Dan Gomez Blanco** 01:55 Good good just trying to put the agenda for today.
but I'm not sure I don't know if I'm assuming that Adriel or Dawson will be joining.
**Martin Costello** 02:51 I don't know, is the short answer. So sometimes sometimes I've come to this egg, and no one else has turned up.
**Dan Gomez Blanco** 03:03 I think I mean I couldn't attend the last few ones.
**Martin Costello** 03:12 I can't remember when from, but I think so. Someone is on holiday this week and next week, but I've forgotten who it was.
**Dan Gomez Blanco** 03:23 All right.
Yeah, I see the I've been already starting to have a look at the at the project proposal.
I'm just gonna kick here as well.
so I guess the phase 2 right
**Martin Costello** 03:46 Yes, I think I think got shared about 2 weeks ago in the Sync, and I had a quick look through it. But I'm relatively new. I just read it, and it seemed fine to me.
**Dan Gomez Blanco** 03:59 Cool. I did have an initial review. Yeah, I did leave some comments in there. I'm not sure if Adriel or Dalton or anybody else, I guess.
Good time.
**Martin Costello** 04:12 I seem to remember.
After I reviewed it I saw some someone leave comments on it. Maybe it was you.
**Dan Gomez Blanco** 04:24 Yeah, I think, we're about to.
So I think this still worth creating this, even though, like, yeah, I can check with the Tc. As well. If Carlos and Josh are still basically willing to be Tc sponsors, I think it shouldn't be a problem, because this Sig already has a you know, it's an ongoing sig, so it should. Shouldn't be a problem in terms of like the phase 2.
so I can. You know, if this is being recorded, I can probably explain where I'm going with this, and I'm not sure if you're familiar with the project management and of open telemetry, and how things you know work in that sense.
**Martin Costello** 05:08 Only vaguely, I've not got involved in cross, sick.
**Dan Gomez Blanco** 05:14 Yeah, the idea is well, for when you're forming a new sig, which was a phase, one of this that needs some type of like let's say approval or or you know, governance around the formation of a new Sig. The project proposal is a way for us to be able to to ensure that that that projects are staffed and that Sigs are staffed.
And they are. They've got everything they need to succeed. Basically, we've got like leadership involved.
We've got community. We've got people that are going to be working on it as well, which is probably some of the aspects that in this second one I wanted to discuss was the.
you know, when we phase 2 so like if we can reach out to. And I can help with that as well, maybe reach out to more of a Cicd industry to.
you know, to see who's because I think one of the things that was called out is like adoption of these semantic conventions and adoption of this in in different, in different places. Right? It will be good to be able to have someone, let's say from I don't know from you. Name it Github Jenkins.
Gitlab Team City, whatever to basically say, Hey, you know, we're in this, and we'll be supporting those semantic conventions and or looking at like a prototype of like of that. I think that was called out in the project proposal. So just wanted to see, you know the if we could have, if we could have some names on on there, people that will be joining.
That would be good, because there was already a lot of good work being done as part of phase one.
And then we can say, Hey, we got some folks together. We deliver some stuff. If we can get more people we can deliver more things.
So so that's the idea. However, having said that after the seg is formed, basically. And you've got a project. You've got some deliverables. This is why phase 2 is now being discussed.
we you know. Not every Sig needs to have a project going like in this case. The Sig. The Cicd Sig is a little bit different, because it's a cross-cutting thing like, we want to get implementation in different languages or implementation in the enterprise eggs. Or we use we, you know, with dog food.
these conventions into things that we monitor in opentelemetry. So I think it's still worth creating this project, and not just sort of like going into our ongoing zig BAU style of work.
Long story short, I think it's a good idea to create this project proposal and ensure that we've got the right, the right people involved basically.
**Martin Costello** 08:21 Yeah, yeah, that makes sense. Cause. What I've said in 6, I've been in the past is like.
for example, I will do a lot of work in the.net space, and I'm a Microsoft, Mvp. So like I could help try and get sort of it baked into the.net part of the ecosystem. That's where my skills lie, and I use get up actions for like my Ci stuff. But the missing bit, at least for me. Just a cursory level is like.
how would you get any metrics out of the Ci in Github, even if you had the the language support to actually look at the data.
or at least do it in an easy way, because, like, where's the collector gonna be.
**Dan Gomez Blanco** 09:05 Yeah, yeah, exactly.
I think the current, I mean hopefully, that will be. You know that to me is the the end goal. Right for someone not to have to, potentially, you know.
even have to run a collector to be able to get like push metrics from Github or Gitlab into a back end.
If you just point the if you could configure it, let's say hotel export in one place.
But yeah, I think.
**Martin Costello** 09:41 Because, because yeah, cause. Another thing that occurred to me is sort of like, if I wanted full visibility in my Cicd.
But there's random people on the Internet doing Prs to me. I don't want to give them access to the credentials of my collector.
**Dan Gomez Blanco** 10:00 Yeah, of course. Yeah.
**Martin Costello** 10:01 For that. But I still want to observe the data. So then it's like, how do you solve that problem?
**Dan Gomez Blanco** 10:07 yeah, definitely, yeah.
**Martin Costello** 10:10 I. In fact, I discovered just this morning that someone internally Grafana's set up Cicd tracing somewhere. But I have no idea how it's been set up, but I think it assumes using self hosted runners.
So it's.
**Dan Gomez Blanco** 10:31 Oh, yeah. Well.
**Martin Costello** 10:31 Near the runner, but with one extra collector attached to it, and then that's going off into a cluster of us somewhere.
**Dan Gomez Blanco** 10:39 Yeah. So that's 1 of the things that I worked with that in the past as well of like, you know, observability of runners. And you know the metric. I think they only support Prometheus at the moment. So that's probably, you know, like so like the the metrics from the runners themselves. You can. You know they have, like Prometheus, export But again, you know not sure if those are following.
probably not following any semantic conventions at the moment from the hotel side in the metrics that come out of the runners.
And yeah, not sure about that again. You know, it's 1 of those areas where ideally you would have a you would be able to use standard hotel config to configure what you push that data right? Or more.
**Martin Costello** 11:27 Yeah. Cause I guess thinking out loud is like, ideally in Github side. They put the collector on the agents that you just get for free configured to push to some internal Github proxy collector, and then it could pro proxy them off to somewhere else. You configure in your repo settings.
**Dan Gomez Blanco** 11:50 Yeah.
**Martin Costello** 11:50 But that's the sort of thing that needs people to get up to build. You can't just Pr into. Get up.
**Dan Gomez Blanco** 11:56 Yeah, yeah, exactly. Yeah.
All right. So I guess.
Yeah, if not, not getting a Dolton or.
**Martin Costello** 12:10 I I saw Adriel said in slack that he can't make it.
**Dan Gomez Blanco** 12:14 Alright. So I guess the yeah, there there is that document or that project proposal.
good to, you know. Be good to get that, you know the comments addressed.
or at least people to comment on that and say, Hey, ob I'll be So I'm just trying to think of the staffing and responsibilities we've only got for now.
Dalton and Adriel signed up in that.
And let me just add a comment there.
And yeah, we'll need to get more folks in, you know, to sign up to this phase 2.
And guess, Martin, if you're like up for it as well, and to basically say, Hey, you know, you've just mentioned something there, I would. If you've got a particular area that you want to focus on, like you can say that there as well in the project proposal, saying, You know, oh, yeah, I will be, you know.
I'll be happy to join, and you know in this, and I'll help. I can help in this area. That would be great, too.
to have you know, to have that in the project proposal. The strong the more people in there, the stronger the proposal is. Right? So yeah.
I'll leave a comment. There's a there's a name. There's a place called Staffing Responsibilities, and it says team structure. At the moment it just says project leadership, Dalton and Adriel. But would be good to have more folks a lot of comment there, so we can add a section for that.
because we don't want that.
**Martin Costello** 13:59 But that's probably why I didn't think to do to suggest anything, because.
**Dan Gomez Blanco** 14:02 Yeah.
**Martin Costello** 14:02 Sponsors. And that was it.
**Dan Gomez Blanco** 14:04 Yeah, a lot of comment in there say, like, we need more, as you know the rest. I guess I'm not sure what to call it, but, like, you know, like rest of people that will be contributing.
**Martin Costello** 14:18 Hmm.
**Dan Gomez Blanco** 14:18 So contributors. Yeah, in different areas, as you said.
cool, awesome. Alright. Well, I guess we can.
We can go and comment on that and try to move that forward.
**Martin Costello** 14:34 Okay. Cool.
**Dan Gomez Blanco** 14:36 I'm not sure if you had any other topic that you wanted to raise.
**Martin Costello** 14:41 I was just gonna mention the fact that I discovered we had something set up internally. I've I've asked whoever sets it up to like.
catch up with me. Explain how it works, because because I don't think I can share it. But it's effectively. It's it was Grafana traces, and it showed the workflows and the jobs and steps, and then it linked off to all the logs that have been ingested. No idea how they got in there.
It looked like it had. It seemed to be following the scientific conventions. But I'm no expert on them. So whether they're actually correct is different question, but it it looked like it was mirroring the Github Ui.
but in Grafana, as traces.
**Dan Gomez Blanco** 15:25 Right.
So it wasn't the runner metrics. It was the actual traces from from workflows and.
**Martin Costello** 15:33 Yeah, yeah, cause it, it had like a nested spans. So you could see, here's the job. Here's the steps. Here's the logs for those steps.
**Dan Gomez Blanco** 15:41 I wonder if they're using already the the Github receiver.
**Martin Costello** 15:46 There's there is. They did share a link, saying they were using the group. There's a Grafana Hotel Cicd collector.
which which, so it makes sense that something is sending data to us, and then it's going off into a grafana setup. But, I've no idea what is pushing the data to it, and how it's configured, and where it's getting the data from.
**Dan Gomez Blanco** 16:09 Because there is one Github receiver that basically gets the web hook from you. Just configure that at a repo level.
I think configured at an org level, as well.
**Martin Costello** 16:20 Oh, so it's sort of like using the web hooks to then go and scrape the data and then push it in.
**Dan Gomez Blanco** 16:27 Yeah. So basically, the the collector gets the the credentials as as an app, I think then you can use it as an app as a github app, and then gets the the web hook, like the receiver in that case is is does 2 things. The Github receiver. One is like. Get the metrics from like related to get repos.
Things like, you know, Prs merge and blah blah the Vcs metrics, and then it gets the and it has the web hook to receive.
Yeah, I guess I request per like workflow execution, and then it goes back to Github to retrieve the details from it, right from that.
from that execution. And then it does the. It builds a trace. From that.
There were many solutions.
That's right. Okay.
floating until this was built in the collector as a as a component, there were many solutions floating around, so maybe you know, some of them did like logs as well locks and context as in, you know, basically with the trace, id and span id. So you click on one of the steps, you will be able to see the logs for that particular step.
So the span is a step, and then you have the logs for that.
And so there were many solutions out there. Then this was built, but I think it's lacking logs, and so.
**Martin Costello** 17:49 The thing I looked at today definitely had logs, but they weren't in line in the traces right? There was like an icon next to the span, which is like click to see the logs, and then you went into a different tab, and it showed you the logs.
**Dan Gomez Blanco** 18:00 Right? Right? I see. Yeah. So maybe that maybe that's using a different receiver or a different, even a different thing altogether. There was another solution that relied on adding a new, like an extra workflow step, or that basically would execute at the end of the of the workflow.
And then.
**Martin Costello** 18:24 Right? Okay.
**Dan Gomez Blanco** 18:25 Generate the trace.
But you know, that wasn't like, for example, here in new relic, we had an experimental. It's still out there. Basically, I know that people are using it. That does that, basically. But it does rely on the person that is doing. The instrumentation of is the person that's defining the workflow to add that extra step right? Which is not always even possible to add an extra step to your workflow, to be able to export tracing log data.
**Martin Costello** 18:55 Because is it like? For, like a full end to end of everything like at least in the context of like stuff I do with.net is like the missing bit seems to be.
How would you be able to give the parents span to the build so that then you could get the granularity within the build, so like the the one I saw today, only goes as far as the step.
so it it goes as far as build your code.
**Dan Gomez Blanco** 19:25 Oh, I see!
**Martin Costello** 19:25 You had, like a custom build logger, you could go. I'm resolving the dependencies. I'm collecting the files, and you go even deeper. But if it was all being collected after the fact through web hooks.
you wouldn't have any like parent span to be able to correlate the things together later.
**Dan Gomez Blanco** 19:46 Yeah, yeah, I see what you mean. It's a good point. I don't know exactly how that's being handled at them. I know that there is. Well, the one thing that I will need is that context propagation by environment variables that's been married as part of phase one I don't know if that's being used right now in any prototypes or anything. That's you know, that's using that. But I'm assuming part of the solution would be, would be that right, having a trace Id in there at this dart.
and then you propagate that by environment variables to your build, and then somehow, you pick it up later. I don't know. Maybe something like that.
But yeah.
**Martin Costello** 20:29 Yeah. Cause I, ideally, once you've got that, you could collect, build and test data and then correlate it all later. And then, you know, if you've got to build with a flaky test.
you can pull through this the trace and then go. It's when this happens. That's why it fails.
**Dan Gomez Blanco** 20:47 Yeah, yeah, that would be that would be good. But yeah, I think, I yeah, I'll defer to Adriel. I think that's he's probably gonna know more about the status of the implementation of those things. But it's definitely in the roadmap, right.
**Martin Costello** 21:02 Okay.
**Dan Gomez Blanco** 21:05 Awesome.
Okay? Then we got someone briefly join in there. But they.
**Martin Costello** 21:12 Joined and left.
**Dan Gomez Blanco** 21:14 Okay, cool. Well, nice seeing you around. And if a lot of comment there, see if we can add a new section, for you know other contributors, and then
**Martin Costello** 21:22 Yep.
**Dan Gomez Blanco** 21:23 Proposal.
Sure, all right.
Catch you later.
**Martin Costello** 21:27 Catch you again. Bye.
