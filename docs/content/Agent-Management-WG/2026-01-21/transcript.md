SIG: Agent Management WG
Date: 2026-01-21
Duration: 56 minutes
============================================================

## Zoom Recording Transcript

**dpaasman** 01:49 Ed.
**Tigran Najaryan** 01:50 Hello.
**Evan Bradley** 01:56 Hi, everyone.
**Tigran Najaryan** 02:01 Pardon me.
Okay, I think we should go ahead.
I guess before we start with the agenda, a quick update. Michael is now an approver on OprahGo.
Thank you for, for your recent work, Michael.
Welcome.
Okay?
Cool. Okay, let's go ahead with the agenda. Braden, you have the first item. I know you have only 10 minutes, let's go ahead.
**Braydon Kains (Google)** 03:35 Yep.
So… I posted a document in the OpAMP Supervisor Slack channel, take a look if you haven't read already. The gist of it is that I've been working, with the folks at BindPlane to try and come up with a solution for our product, the Google-built OpenTelemetry Collector, to be effectively integrated with BindPlane, and that comes down to… we need to have an effective path for users to onboard to the Avamp supervisor.
The problem we're running into is that our primary method of distribution is a package manager package for… for… VM deployments.
And… how to get the supervisor in that case, and how to reconcile supervisor-managed op-amp updates, I could not find a way to reconcile the fact that there would be two sources of truth from an op-amp update and from a package manager update, and the fact that they could skew out of sync led to too many, like, hypothetical user experience problems. I wrote a gist with the specific scenarios I tried to see if I could find a way for this all to fit together, but I couldn't really come up with any. And Dakota, maybe I'll hand it off to you, because we talked about it yesterday a little bit.
**dpaasman** 05:00 Yeah, yeah, so I can… I guess I can kind of speak to… Kind of… my experience and experience that we've had at BindPlane on this topic.
Because our… so our version 1 distribution of the collector implements this, the idea of upgrading via op-amp. And this is definitely something that we've had issues with. You know, we generally recommend to customers to either stick with package-managed upgrades for the collector, or stick to just op-amp upgrades. Because, yeah, they get out of sync very easily, and there's no great way of reconciling them.
We know that there are customers that prefer to use package managers for upgrading the collector.
But we also know that there are customers that want to use OpAmp for doing that.
So, it makes it a little tricky because, yeah, you've got these two avenues, And they just… they don't get along very well.
And so we were kind of discussing that yesterday. We… like I said, we don't really have a great solution. We… Talked about maybe having you know, whatever's doing… because this is independent of the supervisor, this is just a problem with op-amp upgrades in general. Whatever's doing the upgrade for op-amp.
Maybe there's a way that it can use the package manager for doing that upgrade.
That way, you know, there's no difference between, you know, what the package manager is expecting, what op-amp is doing.
That feels a little tricky, though. Braden, I don't know if you have… Anything more to add there?
**Braydon Kains (Google)** 06:47 It feels like a can of worms, just because different package managers operate in so many different ways, and to anticipate them all would be quite a challenge for OpAMP to to work through.
**Tigran Najaryan** 06:59 Yeah, so I think I see, I see two… broadly two possibilities here. One is what you were describing, Dakota, and what Ellen was suggesting, is that they're mutually exclusive. You choose either the operating system package manager or OPAM.
one or the other, but don't mix both, right? But I can also see another possibility here is… probably the reason why people want to use the operating system package manager is they already likely have an infrastructure in place to distribute something to the machines, right? So they are… they have, I don't know, Ansible, Puppet, or stuff like that, which allows them to push RPMs to all the machines they have, and then you use that as means for initial distribution for your collectors.
But then you want to use OPUMP and the facilities it provides for upgrading the collector.
So, I think it… it is… to me, sort of a reasonable expectation that, yes, I do have the infrastructure for initial distribution, but I still want to use the OPAMP.
upgrading capabilities. I think there is a way to do that, actually. And… and this is, like, from the top of my mind, it's probably a bit more thought. What you could do is, in your initial distribution.
Package both the supervisor executable and the collector executable, But… Upon the installation of the package by the operating system package manager, make sure that the collector executable is placed in some sort of an initial location, and the supervisor Upon the first startup, Copies it to the permanent location.
And from there on, the… the open package management takes over and updates the collector executable in that location. Any subsequent updates pushed through the operating system package manager will update the supervisor They will also update the collector binary in the temporary place, which is no longer active.
It will have no effect on the collector binary, so you're essentially opting into the continued updates of the supervisor executable through the operating system package manager.
and opt out of those updates through that channel, and instead, the subsequent updates to the collector executive will happen through the OPAMP package management. So that sort of combined approach is possible if you're deliberate about it, right? That's… if that's… That's the goal, right? I can see where that scenario would be useful. I am giving you a way to the initial distribution through your existing mass deployment capabilities. You use your Ansible or equivalent, and it doesn't really matter what exactly is the package manager, as long as you follow that pattern of this collector executable is packaged inside it as sort of a data file, which I'm going to copy on the first startup and mark it as an executable, and now I'm going to take over the management of it.
Now, when I'm saying I am going, that supervisor is going to take over, and then from that point on.
the open… package management kicks off and starts doing the collector handling. The additional, I guess, benefit of that is you can continue pushing maybe supervisor updates through that.
And maybe there's a variation of that also, where you do similar copying of the supervisor, and then you handle the supervisor upgrades also through, maybe, OPAMP package management facilities.
So this is just sort of a very, I guess, quick idea. Needs to be… needs a proper design, obviously.
**Braydon Kains (Google)** 11:14 Yeah, that makes sense. I think we… we discussed something similar, like… like, we have a… we have another product to distribute through a dead package, and, like, we distribute a default config the first time, but we never update it on future updates, so, like, there is some… some sort of precedence for treating something as, like, a data file that doesn't get continuously updated through package updates. So, that is a… that is a reasonable way forward.
I guess I'll need to think about it a bit more, because from our side, we're not… we were… I was trying really hard to find a way where we didn't need to create our own supervisor plus collector package to be able to distribute this.
really tried to make it into two packages, where the supervisor is one that can be sold independently of any collector package, but I really just could not think of a way to make that work.
**Tigran Najaryan** 12:01 I think your design likely needs to follow from what exactly is the goal? Why do you want to use both package management systems, like, both the operating systems, package management, and the OPAM, right? What is the end goal here?
And my guess here is that you use the package manager for the initial distribution, and the OPAM for the future updates.
But it's just a guess I'm making here. If that's the case, what I was proposing maybe will work, but your goals may be… may be different than that. I may be guessing wrong here. So, I guess that would be the question I would ask. So, why… why am I… why do I need both systems in place? What is it that I'm trying to achieve here?
**Braydon Kains (Google)** 12:47 Makes sense. Unfortunately, I'm out of time, but thank you very much for discussing this, I appreciate it.
Good discussion, and I'm happy to talk about it more.
**Tigran Najaryan** 12:55 Sure, yeah. If you want… I guess you have… I saw you had that document in GitHub. Maybe open an issue in Opump.
call repository.
Or somewhere in the… in the collector contribository, so that we can continue the discussion there.
**Braydon Kains (Google)** 13:11 Sure, makes sense. Will do. Thanks, everyone.
**Tigran Najaryan** 13:16 Alright, thank you.
Sure, let's move to the next one.
Joande, you want to talk about the… server example, the API for the server?
**JM Juande Manjon** 13:31 Yeah, so, this is if we are to add the REST API to the OpenS server example.
Basically, this recipe, I mimic the current UI features.
And it will provide, especially for, PLCs, people want to adopt OPAM.
a REST API that they can play around the server. That could be a CLI tool, could be a modern UI.
I think it's interesting to have the REST API And the point is, to grant House and consent that who will maintain that.
Actually, it does belong to the core of Ancore, because it's an example on the server.
Could be a good time to have, you know, pinecone trip.
Where people can work on independently to the core of PAM.
So, yeah, actually, that PR is actually blocked, I understand the consent, so we need to find a way how we can handle this.
**Tigran Najaryan** 14:31 Yeah, just to be clear, right, I think it's valuable to have more comprehensive examples. I'm not opposed to that.
what I'm worried about is that that's a… significant amount of new code that we have to maintain, and as a maintainer, I don't want to take that responsibility, to be clear, right? I want to do the bare minimum that I need to do to produce the OPUMP library here. And to me, that means the OPUMP interruptions. Examples are great, are useful, but if if I can find a way not to do it, that's a win to me, because there's a lot more that I need to do at OpenTelemetry. Now.
I think, in my mind, that crosses the bar of the minimum that I need to have as an example. What you have is nice.
But it is nice to have, not need to have.
Sort of an example.
So, I would really either want one of the maintainers or provers to commit to maintaining it long-term.
And then we can take a look at accepting it, or if that doesn't happen, then we find a different place for it, right? And I'm then happy to link to it.
And promote it, but not be on the hook to maintain it long-term.
**JM Juande Manjon** 15:51 Yeah, so the thing is visibility for other, for the community to see the example.
could release internals. I think it's not the right place, but…
**Tigran Najaryan** 16:05 Yeah, if you make it a different repository, it also doesn't have to be sort of an internal package in that case, right? You can place it wherever you want, can be a… Top-level packaging as well.
Does the example need to be in OpenTelemetry? I think that's… Probably, yeah, open, we can discuss that.
But, like I said, if we do not have An existing maintainer or approver.
say, yes, I will maintain it, then I don't think we should Place it.
inside the… this particular repository. It can be a different repository, and maybe that can be… a different repository in silo on telemetry, so it doesn't have to be somewhere completely outside of hotel, but that we will need to probably discuss separately.
So, what I would advise is maybe let's give it a bit of time for… Existing maintainers, approvers, to… See whether they want to be that person who… sponsors, essentially, we have that model in the collector, right, Antoine? When, if there is a new component proposed, you need to have somebody existing who becomes the sponsor of it, so if somebody's willing to be the sponsor, then I think that's okay, we can go ahead with that. Let's give it a bit time, a few days. If not, then let's figure out what's the alternate, where else we can place the example.
**JM Juande Manjon** 17:39 Right, definitely, the example are… I'm tricking, I mean, attention to other people, so the next item, Michael, is gonna work on that, too.
So people is looking for a plan, so if we have this basically more visibility, where people can contribute.
contribute to this, I mean, everybody will be happy adopting OPAM, but Example is very good to see how it's going, especially for people doing POC. We have seen people having different survey implementations, so many people working in different directions. We have a place where we can work together. I think it could be better for long term for the OPAM.
**Tigran Najaryan** 18:20 Yeah, well, I agree, not push back on that, right? Let's just find the right setting to place the example, and I would really want to have that, yes.
**atoulme** 18:32 Yeah, so for the collector, just to give you a little bit of contrast, we actually have rules to allow only new components if they have a sort of sponsorship from a prover maintainer.
And those rules have been strengthened, recently. We actually ask now that the code has already been committed, made open source, and is somewhat in some active shape by the time that we allow it into Contrib.
Because we are running out of bandwidth to kind of get the kinks out of some of the code that we see out there.
We really encourage also people to kind of self-host, and own their own components, and build their own collector distribution, because we have tooling for that, it's something that's well supported, so you would be able to do that. For your use case, I see two very clear paths. One is you contribute enough to OpenGo, you become an approval maintainer, and then you can push that code in.
That's an easy one.
Another one is you petition for that contribute repository you're talking about, which might be an issue with a community project, to ask that we, you know, enlarge a little bit the scope of the SIG, and you also petition at that time to become a maintainer of that contribute repository, which means an engagement from your part to maintain that code moving forward.
There's another path you could look into, which is the OpenTeometry demo is a great place for helping people with POCs, or people who are getting started with OpenTeometry. They might be receptive to the idea of having some function of the demo.
To show agent management, through some sort of an example, and actually productize that as part of the demo script in the demo environment they have.
**Tigran Najaryan** 20:13 I actually love that, Antoine, that proposal. We can't put an example of OTAMP implementation inside the OpenTelemetry demo, because we have all sorts of things in the demo, and the point is exactly that, to have everything that is possible in OpenTelemetry in that demo. So, maybe that's actually not a bad idea, I like that, yeah.
**atoulme** 20:35 Yeah, me too.
**JM Juande Manjon** 20:36 Agreed too, so, yeah.
I, I will… I will reach you later to see how… how we can do that.
**atoulme** 20:45 Sure.
**JM Juande Manjon** 20:49 Thank you.
**Tigran Najaryan** 20:49 Okay, okay, cool. Let's move to the next item, then.
Michael, you have the next one.
**Michel Laterman** 20:56 Yeah, so… based on feedback, I'm not seeing the scale test mode I've added.
is now ready for review. I've added a behind flags in the example agent, so… the… One aging process would now be… Capable of starting Thousands of fake agents to an example server.
Ideally, this mode would just help us Have some basis where we can… Scale test different server implementations, or if we wanted to consider changing things like the WebSocket libraries, we would now have a tool to test How performant that change can be.
And the smallest thought I have is… I've… Moved out the… example metrics I've added to the example… to the server, into its own PR for separate reviews.
The better contain the scope of each.
feature.
**Tigran Najaryan** 22:09 Yeah, I did take a quick look at the PR need to do… to do it again, and we updated it. I guess, maybe, first things first, in the spirit of applying the standards uniformly, you are… you are going to be the sponsor of this… In the… in the repository, who is going to be the sponsor?
**Michel Laterman** 22:29 No, no.
I think it's pretty easy to sponsor this one, because it's…
**Tigran Najaryan** 22:38 Okay, so you'.
**Michel Laterman** 22:39 Not… yeah. You're taking it Okay.
**Tigran Najaryan** 22:43 Cool, cool.
Otherwise, I think the direction you're moving in is the right one. You're refactoring the existing agent and reusing it for the scale testing, I think that's the right approach.
I'll take another look at the PR.
I didn't have a chance to see what you have changed since I last looked.
Okay, any other comments, thoughts?
Anthony?
**JM Juande Manjon** 23:21 Oh, I've been… I've been looking at my core PI, I get to provide some feedback, it looks… I think it's ready for pushing.
But I don't have, I cannot approve it.
For Mercury.
**Tigran Najaryan** 23:34 You actually can. Anybody can approve, it just… it's not going to count against the minimum approvals requirement for merging, but it still helps.
To get your approval.
It's a validation that you find the feature useful, you have looked at it, so… Anybody who's actively participating in the SIG is welcome to give their approval. It does have a weight, doesn't really matter that you don't have formal approval requirements.
**JM Juande Manjon** 24:05 Okay.
**Tigran Najaryan** 24:06 So when… when you… when you're ready, feel free to approve.
**JM Juande Manjon** 24:11 Sure, thank you.
**Tigran Najaryan** 24:18 Okay, cool. Let's move on. A quick update, there has been polling done to change the time of this call.
It was in Slack. I don't know if… Everybody had a chance to take a look at it. I pinged the maintainers, approvers. Michael, I think you were not an approver when it started, so maybe you need to take a look at it. There is a pull request with a new proposed time there.
So, hopefully, Well, unless we find a blocker, we accept the new time.
So take a look, I put the link to the PR there in the agenda.
That's mostly to make it a bit more usable for people from, I guess, outside the North America, from Europe in particular.
Okay, let's move on. Is Israel… is Israel here?
**Israel Blancas** 25:24 Yep.
I'm… Yep.
Yeah, hi, thank you. I think it's the first time I joined this call. So, well, I'm coming because the thing is that we have been using… well, we are using OpenMP a lot.
Something that we noticed, right, because we have been… I mean, right now, we are using the supervisor, right, to send to receive the configurations and everything, right? And one of the things that we've found is that sometimes when you want to… When there is something that is failing, right, or something, when applying a configuration, or something like that, sometimes the error messages that are received, right, in the server.
can be a little bit tricky, right? To, like, to reconnect them as an error or something like that, right? It's like… Maybe you have to do some parsing, right, of the logo and things like that, right? Something that we would like to, have, I will be more than happy to contribute. It's, a new field, maybe, right, to the protocol.
like, something to have some kind of a structure, arrow thing, right? In our case, I mean, I have been taking a look maybe in Greenwright, but, we think that the best location For that will be to add it to the component health message, right?
I created this message, this ticket, on December, and also one… another ticket in the OpenTelemetry Collector Country repository, right? And even I sent one… draft beer, right, with some ideas, right, of all these… look. Yeah, it's like, I come to this… Just to see if there is any… thing against doing this, right? Before I do, Maybe a pull request or something like that, right, with some proposal about how this bill could look like, or something.
**Tigran Najaryan** 27:25 Okay, Evan, can you remind me something? Does Supervisor today… collect the collector's logs and send anywhere. Is that implemented anywhere? I think we had that as a capability described somewhere, but I don't know if it does exist.
**Evan Bradley** 27:43 It configures them, but it doesn't proxy them. I think we might have discussed that at some point, but from what I recall, the collector will send them directly to the backend.
But I think that that would be the sort of way that I'd want to see this implemented, would be using, like, configuring the collector's logs, maybe proxying them, and then forwarding that on, if it does, work, or linking it in the, what do you want to call it, like, the telemetry backend, or… I don't know, I'd like to see that integrated. I would feel a little strange if we duplicated telemetry collection in the spec.
**Tigran Najaryan** 28:22 Yeah, and the reason I'm asking is I'm thinking whether that rush report belongs to the logs then, right? If we… If we implement the collection of the logs, then all you need to do is just put the additional brush details as another log line, structured log line.
And that should probably achieve what you want here, right? I'm a bit… I'm a bit worried that we are implementing an alternate telemetry channel by adding all these capabilities to the component health.
And it's not entirely clear.
what is the line there, right? What is the litmus test? But when I'm thinking about the crash data, I'm thinking about logs usually, right? Unless it's about huge crash dumps, which probably need a different delivery channel.
If it's about, like, things like stock traces or something like that, then probably what you want to do is just it's the last line in your log, right? Probably. And then we have a means to… or at least we had a vision of how we would deliver the logs. So the supervisor is there, your collector executable crashes, the process crashes.
Either the collector, when it crashes, writes the last line to the log.
Or somehow the supervisor, through whatever means, is able to figure out what are the crash details, puts them In that same log, so I want to avoid creating more mechanisms for delivering telemetry, and to me, it seems like logs could be that one mechanism into which we could also put the crash reporting.
**Evan Bradley** 30:07 Agreed. Dakota, I actually just remembered that we are, we do have something to buffer the collector's, output to STD out and std error. Dakota, do you think that there would be a way we could capture that and forward it along somehow?
**dpaasman** 30:22 Yeah, I was gonna say, it's not… this exact issue, but I had opened up a PR a few months ago that basically just collected the last standard error message from the collector and sent it over op-amp.
And I think… yeah.
**Tigran Najaryan** 30:40 Something like that, or adding on to that would…
**dpaasman** 30:44 Would work really well here.
**Tigran Najaryan** 30:47 What happens today, Evan, with what you're describing? Do we just kind of interleave the collector logs with the supervisor output? Is that what happens?
**Evan Bradley** 30:56 I think so… Dakota, you would know, you're the one that implemented it.
**dpaasman** 31:01 Yeah.
**Tigran Najaryan** 31:02 You see both the supervisor logs and collector logs in the output of the supervisor.
**dpaasman** 31:09 Yeah, it's with a special flag called pass-through logs, or something to that effect. The intense behind it was to allow the supervisor and collective to run a container environment with just one standard out. But I mean, yeah, it can be used anywhere. It's exactly that. You just see…
**Tigran Najaryan** 31:26 Okay.
**dpaasman** 31:26 The collective and supervisor logs intermingled.
**Tigran Najaryan** 31:29 And do… we don't… we haven't implemented the processing of the offer that then comes through the OPAM to send the logs to a particular destination. That is not implemented.
Today.
**dpaasman** 31:43 That, I'm not sure about.
**Tigran Najaryan** 31:46 Okay.
**Evan Bradley** 31:50 I can't remember either.
**Tigran Najaryan** 31:52 Yeah, yeah. I think… We should probably do a bit more investigation on what happens right now and where we are with logs.
it's possible that that's not the best way to do it, but so far, I'm leaning a bit towards that.
If you have a crash report, put it in a log, use whatever available means you have to deliver that log.
if… If you have… Specific requirements about why it needs to be in the component health?
Vet point.
We can also discuss, but if you only want to have it somewhere, then logs seem to be not a bad place for it.
**Israel Blancas** 32:34 Yeah, no, the thing is that, we've found that people are, well.
We are kind of offering, right, the logs and everything, even from the supervisor right now, it's like, you deploy the supervisor, it deploys the… the collector, right? And from the collector itself, using the 5… They can use in the file or receiver, right? We are parsing everything, even the logs from the supervisor. So if you… deploy your configuration that is not working, right? You are not gonna get, that communication, right, with the… with the telemetry backend, because you are not gonna have a way to send the logs, right? So we were trying to do that as part of the OPMP thing, right, because it's the… the breach that we still have. Yeah.
Yo.
**Tigran Najaryan** 33:21 I get it, but if you look at OPAM, it specifically has provisions about how to send telemetry from the agent, right? It says this is the way. You're supposed to configure your agent to send its logs and metrics.
to a particular destination, so it's… it's not like it's completely outside of the OPAMP scope. OPAMP already has an opinion about how to handle these things. It's through a separate telemetry channel for the logs in particular. So, my advice here would be to maybe… for you to do a bit maybe research, look into what Collector does today in terms of those logs that we're discussing.
And… and also do a bit of thinking on your end to see whether… if crash reporting was added to the logs, that would fit your needs.
And maybe then continue the discussion on GitHub. Based on what you find, we can see what's the right way to move forward.
**Israel Blancas** 34:21 Okay, just, just one thing, the, the thing that you mentioned that could be, be a, would be, like, to have… just, like, report as part of the login just the crashes, or something like that, or… because I didn't get it, right? Sorry, because…
**Tigran Najaryan** 34:35 So, we have the regular logs that the collector outputs today, right?
regular operating logs.
**Israel Blancas** 34:42 When the collector crashes, I mean, it's probably… it panics, right? If it's a go panic.
**Tigran Najaryan** 34:47 we could have that panic output written into the… I mean, it probably does that, it goes to the standard output today, that's… that's what it does by default. And like I said, we have plans, or had plans at least, for supervisor.
To catch that output, and… Sent to the… To the, to the telemetry log destination that was That was offered by the OPAM survey.
So if that happens, you probably don't even need to do anything, because the panics, I think, are already doing the stack traces and all that stuff is output. Unless you have some other needs to include more other information into the crash report.
I don't know if you have, but then would need to look into that.
**Israel Blancas** 35:33 Okay.
Yeah, thank you.
**Tigran Najaryan** 35:37 Okay, I'll increase.
Anyone else, any thoughts on this topic?
Okay, then you're next, Antoine.
**atoulme** 35:56 So it's actually a good transition.
So, there's the PR Open, it's been open for a while. I get, Open Supervisor D, which, adds a feature which, I think it's, impressive.
Pursive idea of being able to have a fallback configuration in case something happens when you update the configuration as a collector, so you have a way to kind of fallback to something that is well known, that works.
And I'm guessing, from what I'm reading in the PR, you fall back, and then you then can update again to a new configuration.
There's a lot of ins and outs of it.
there's some.
**Tigran Najaryan** 36:38 What does… what does… what does it mean for something to happen? What exactly is that? Something?
**atoulme** 36:46 If the collector was not to start properly upon updating its configuration, you would have a way to switch back the configuration to a fallback, which is a well-known config file with some hardened capabilities, so it's less likely that it will, you know, bite, so that you can…
**Tigran Najaryan** 37:03 The failure to start, you're saying? And that failure, how… I'm guessing we put some sort of time limit on what it means to start successfully, or fail.
**atoulme** 37:15 Yeah.
**Evan Bradley** 37:16 I want to jump in here real quick, sorry.
The functionality in that PR, unless it changed last I looked, is a little bit different. It's more so about connection to the op-amp server. So if it does… if the supervisor can't connect to the op-amp server, then provide the collector with this fallback configuration until the connection is made and a config is received.
**Tigran Najaryan** 37:39 Okay, so that's different. The question I have is, why isn't the last known good configuration is the fallback?
Why does it have to be different from that?
**Evan Bradley** 37:50 I think this would be an initial startup. So, if you start up and the, the last known config isn't there, until you… Get that configuration, you can use this fallback.
**Tigran Najaryan** 38:05 Well, then that becomes essentially an initial configuration issue, right?
**Evan Bradley** 38:09 Sure.
**Tigran Najaryan** 38:09 So, you have an initial, The first time you connect successfully.
you receive a configuration that becomes your last known if you apply it successfully, obviously, right? And then that initial is not needed anymore. So that's not a fallback anymore, right? The fallback becomes the… That's true. …whatever was the last known.
So this proposal, then, is about the initial configuration, then, if I understand correctly.
**atoulme** 38:34 You can configure it by giving it an actual configuration to the OPAM supervisor. You tell the Open supervisor.
**Tigran Najaryan** 38:40 Sure, yeah, I get it. That's what you start with, because you didn't have something received from the server. As soon as you receive something, is there any other situation when you can go back to the initial one anymore?
**atoulme** 38:55 I'm actually… sorry, I meant to do this into a meta-discussion, because the problem I'm having is a bit more generic, is that we're adding features to Open Supervisor D, and I think we need to have a broad map discussion about what we want to do with that tool.
**Tigran Najaryan** 39:08 I see, okay. Yeah, let's refund, maybe, let's have that.
**atoulme** 39:12 to me, that's one feature too far that's taking us into an unknown direction, which I'm not sure we can come back from, if that makes sense.
Because it's adding… I don't know, I feel like I'm a little queasy about it. And I documented that on the PR. I said, I can see what you're trying to do.
I think it makes sense from an operational sense, like, you have this problem right now, trying to plug the hole of this.
But it feels wrong. It feels like you're adding one more thing on top of it, like, one more nub on the tool, and I don't know for the life of me if there's a part of due into this that we should exercise here that would give us a bit more leeway into how we want to evolve this tooling.
And, I've been an Open supervisor code owner for a while, just out of, I would say, sheer accident, because, you know, we were looking to get some spread out in terms of, responsibilities, so I have some ideas about how to maintain that code, and I don't feel like I can maintain that feature, first off. Second, I think this is taking us into a direction I'm not sure.
We want to.
**Tigran Najaryan** 40:17 Okay, okay, I think this is good, Antoine. I think this is… this is the opportunity that We want to use to maybe have that discussion about the roadmap.
If maybe… I don't know if you want to use… if you want to put your product manager's hat on, and maybe organize us a bit.
And have that scheduled, that discussion. I don't know if we want to have it as a live call, or maybe we do it offline, but I'm with you. We haven't been organized well from that perspective. After the… maybe the initial designs that we have discussed, when we were just starting.
And we kind of implemented some of it. We haven't reviewed… revised that roadmap at all, so if… if you are willing to maybe help us a bit with doing that work. I think this is… maybe just about time, right? It's been a long time since we looked at what we have, and Where we're… where we're going.
**atoulme** 41:16 Yeah, I'm not saying it should be… I think I can help. I certainly have feedback and maybe some principles we could share on what we want to build here, and what the big pieces should be doing and doing well, and what's not in scope.
I would also make sure that this is not something that I'm, you know, the community here, everybody on this call, you can participate. So, if you look at the PR…
**Tigran Najaryan** 41:41 But the reason I'm asking is because you are a lot more experienced in that type of activity, I guess that is why, maybe.
**atoulme** 41:50 Yeah, yeah, no, I mean, appreciate that. Yeah, I'm not… I'm not trying to shirt the responsibility of trying to come up with something here.
I, I started the discussion of PR in earnest, and I actually put Evan a little bit in the hot seat on where we want to take this, and Evan said that we would be discussing this at a SIG meeting, so this is the next SIG meeting we're having a bit that checkpoint.
I'm not sure we're going to be able to come up with something in 20 minutes, right? But I just want to make sure we… we start the discussion.
**Tigran Najaryan** 42:22 I think we should. I came unprepared for that discussion. I'm not sure I can have a fruitful discussion right now without having I guess, any preparation done.
What if we either plan it for the next call.
Or we don't have to wait, maybe, if we can put together some drafts?
We can start even before that, right? Start doing it offline. What I would maybe start with is… Come up with a draft list of potential ideas.
the ideas that we had in the past, things that are remaining on the current design document that are not yet implemented as well, things that were proposed, like the NPR that you brought here.
and other ideas, put together sort of a draft list, and… and start debating on it, right? See whether it fits…
**atoulme** 43:17 The long-term goal that we have for the project.
**Tigran Najaryan** 43:21 And maybe, maybe separately from that, maybe at least sort of a long-term vision for the project, where we want to take it, and then see whether that… What items on that list match the long-term vision?
a bit, I guess, what I'm suggesting for us to be a bit more systematic and be more prepared. I don't think the time that we have right now works best. Totally open if you guys want to discuss, but I'm myself not prepared.
**atoulme** 43:48 So… I'm clear.
**Evan Bradley** 43:51 Go ahead.
**atoulme** 43:52 No, no, go, go, sorry.
**Evan Bradley** 43:53 Okay. So I have some… yeah, I would also like to see that, because there are… I've seen a lot of feature requests to the supervisor, and honestly, it's been challenging for me to evaluate them on a case-by-case basis without… like, I have an idea of, you know, what we want to do, but it's not written down anywhere, and so… You know, every time one of these things comes up, you know, you have to look at it and figure out if it makes sense, and kind of the idea of what you think the supervisor should look like in your head. So I'd like to get that in writing, also so that we could show other people, because there are a lot of people that are interested in this, and they have a lot of ideas for how this can work. But, you know, like you're saying, we can't just keep… adding on to it, forever. And in particular, the supervisor, I mean, when we set out to do this, you know, we knew that it… there has to be a hard limit, maybe not a hard limit, but there needs to be some kind of limit on how complex it can get. You know, it can't be so complex that it's less stable than the collector, or, you know, it needs to be rock solid. So, if this is, Antoine, if this is a feature that you think is more effort than… or, what do you want to call it? The main… the maintenance and, just, what do I want to say? The complexity of the code are more than the feature's worth. I think it's okay for us to say.
sorry, but, you know, we don't want to maintain this, and you're free to fork it. Unfortunately, we don't have a very pluggable architecture right now, so maybe that could be a motivation for… people to add that. This feature, the reason… and so I did ask, Douglas, the author, to trim down the functionality a little bit. The thing I like about this feature is that you can start up the supervisor and a collector, and even if there's no server, you can have something run. Like, you can know that something will start, and you'll get data until that connection starts. That said, again.
You know, there are other ways of solving this, and if we think that this is, you know, one step too far, then let's, you know, step back and really take a look at it and see if there's other solutions.
As for planning, yeah, I don't know that we're gonna be able to do anything in 15 minutes here, and I'd really like to go through and see what we have first, but I, again, would absolutely love for us to have something written down there, and I would appreciate any, any input or help you can provide.
**atoulme** 46:14 Okay, we're… we're aligned, I'll tell you, maybe from a high-level principles.
**Tigran Najaryan** 46:20 Yes.
**atoulme** 46:21 It's introducing a state that can be surprising for users. And I abide by one principle on that, is that we don't want customers to be ever surprised.
If for any reason there is a disconnection, then the collector may behave in a way that is actually conducive to missing alerts, or missing interesting signals, and I don't quite like this. I think this is… This is, a state of surprise that people might not be prepared for. The fact that it's an optional feature kind of alleviates that somewhat, but still, I feel like people could, you know, fat-finger this and get themselves into a really bad situation and not know that half the collectors are not reporting properly, because they're still beeping on the UI.
So, I, Okay, we need to kind of, refactor this into a roadmap and some set of principles to help us kind of drive this. Yeah.
**Tigran Najaryan** 47:15 I think one of us one of us who is familiar with OPUMP and Collector, both, I guess. One of us needs to start with writing down maybe a page of long-term vision of where we're going, and the principles, like, not the specific items we want to solve, but What is the… generally, what… where do we see the supervisor going? What do you call, maybe, the principles?
I don't know who wants to do that, you guys… Yes.
If you want, Antoine or Evan, if not, then I guess maybe I can also take a look… up to you guys, whoever wants to do it.
We should probably start there, so that we know How do we evaluate all the incoming, I guess, requests as well? That will help a lot.
**atoulme** 48:05 So I have a very famous move, which is that I'm very good at starting things and opening a doc, and then in the dock, I put things which are wrong, and then half the internet, that's something people like to do on the internet, is to tell you that you're wrong.
And usually that creates the influx of community that we need to kind of get where we need to be. So, I'm happy to do a first draft that is going to give a place for this discussion to have.
**Tigran Najaryan** 48:29 Yeah.
**atoulme** 48:30 The most important.
**Tigran Najaryan** 48:31 Antoine, I'm all for crowdsourcing ideas for features and capabilities, but vision, the overall vision, I think we… it needs to be written by somebody.
Who has a lot… I guess, more extensive knowledge of the area, right?
**atoulme** 48:47 Okay.
Yeah, yeah, so…
**Tigran Najaryan** 48:49 But it's probably going to be likely a limited number of people who have the experience, both, like I said, with all pump and the collector.
**atoulme** 48:59 Yeah, I… I'm not that person, but I will sit next to them. I will… I will do the work to engage with them and find out.
Okay. It's not promised, but by the next SIG meeting, we should reconvene and discuss more how that sounds.
**Tigran Najaryan** 49:15 Alright, sounds good. If you want to start that document, Please do it.
ping me when you have something to take a look at, and I'm happy to help if needed.
**atoulme** 49:26 But where would you place this document? The OpenSpec? OpenGo?
**Tigran Najaryan** 49:30 Oops.
**Evan Bradley** 49:30 So, the supervisor has its own spec in the contrib repo. It's in a file under the supervisor directory. I think it's just in specification or something like that. I'm okay collaborating on something else, but I think that that would be a good place for this to end up in.
And, yeah, let me know what, what your internal resource has to say about it, and I'm also happy to help contribute to that. It would definitely reduce a lot of the maintenance burden on my end as well.
**Aunsh Chaudhari** 50:00 And in terms of adding to this, Tigran, you mentioned just ideas there. You also mentioned the design document to kind of patch on to, right, or what we've added earlier. Is that the main…
**Tigran Najaryan** 50:10 That's what Evan is referring to, that design document. It's in the collector contribository.
**Evan Bradley** 50:16 Let me link to it.
**atoulme** 50:17 And the internal person I'm thinking of is you, Ange, of course, right? So…
**Aunsh Chaudhari** 50:21 Yeah, yeah. So, I think that's what I'd like to start off with helping with getting into that depth with this doc, so I'll do that, yeah.
**atoulme** 50:30 I think… okay, so that doc is great. That's, definitely a good start to discuss.
Okay.
**Tigran Najaryan** 50:38 It's also 3 years or 4 years old, so… Kind of due for… for a refresh.
**atoulme** 50:46 Alright, fair enough.
**Evan Bradley** 50:47 We have been updating it when I can remember to ask people to update it, but yes, I think, going through and refreshing it would be good. Plus this is also very technical, and I don't… I think that a… A higher level, section would be…
**Tigran Najaryan** 51:04 Agreed, yeah. And it doesn't have the principles that Antoine was talking about. How do you… what's your litmus test, right? How do you decide something in scope versus out of scope?
**Aunsh Chaudhari** 51:17 Got it.
**atoulme** 51:18 Yeah, these are product high-level goals that I think we can add. Okay.
But yeah.
**Aunsh Chaudhari** 51:30 I can definitely help, yeah.
**atoulme** 51:32 Thank you, Ansh. That… I was going to reach out to you, yeah.
Cool.
**Tigran Najaryan** 51:39 Okay, good.
That was the last item in the agenda. Anything else? Anyone?
**atoulme** 51:49 Beautiful.
**Tigran Najaryan** 51:53 Okay, thank you all.
**atoulme** 51:55 Bye, bye.
**JM Juande Manjon** 51:58 Bye.
