SIG: Specification SIG
Date: 2026-04-28
Duration: 66 minutes
Zoom Recording URL: https://zoom.us/rec/share/kR1XsqFVjO6t3gQrHcXh1Fo_y4joJoU6-u-lWCQTTW26fLUA96AFexyWfDHSL871.WPFfLXK9WD8HzuII
============================================================

## Zoom Recording Transcript

Carlos Alberto Cortez 00:01:51 Hey, everybody. Let's start in a couple of minutes, please. In the meantime, even though we have some items in the agenda.
If there's something you want to discuss, please add it there.
And also, don't forget to add your own names to the attendees list.
Okay, one minute, and we start.
I only see 9 people, I wonder whether there's some event, or no weekend, or what's happening.
Tigran Najaryan 00:03:39 We solved all OpenTeam entry problems, but no work remains to be done.
Carlos Alberto Cortez 00:03:50 Okay, let's start the, the discussion. Let me share my screen in that case, Okay, yeah, so the first item, I don't know whether, Jack, probably you put the item, or I forgot, but basically this is a DC update.
Essentially, we have been getting many security advisories lately, and they have been impacting many, you know, repositories in the organization, and we really want to, request maintainers that you pay attention and, you know, monitor this part of the advisories. You can see it in the screenshot.
what's happening?
Oh.
We have Joe McD here in the call.
Because he was working on a new script to assign cada owners to security advisories, I don't know whether he wanted to give details.
This is, related, by the way, requests and discussion we're having about… regarding, Vulnerability… vulnerability management for, for maintainers.
Jack, you… you want to say something? You have your face that you want to say something.
Jack Berg 00:05:07 face like I want to say something. That's funny. I want to say something most times. So, I guess some color that I want to add to this is, you know, We… like Carlos said, we've seen an uptick in security advisories. I don't think it's a secret why this is happening, the, you know, proliferation of these agentic AI tools is making it easier than ever to detect these.
And, you know, in some cases, it's, you know, it can be… in some sense, it's overwhelming, to get this… what can be kind of a sudden flood of advisories, but, you know, it's also a good thing to find and discover these issues which may have been laying dormant in the code for years and years.
And, so a couple of things that I want to mention. I'm gonna include a link here. We have a SIG security, a security SIG, which is… not that well attended right now, but amongst the things that it has done is it has put together the security response guidelines, and this is where we talk about what the expectations are for all the people that are involved in advisories. So, you know, as Carlos is mentioning, one of the expectations of maintainers is that they are monitoring their own… the advisories that are reported against their repo.
The TC monitors this as well. Whoever the TC member on call is, is going to monitor this, and we'll ping you if, you know, if, you know, you haven't responded, and we can help assist with the process of accepting the advisory, and if needed, ultimately publishing a CVE, or requesting to publish a CVE.
But this is a guide from the Security SIG that everybody should read, everybody should be aware of, just to get up to speed on what the expectations are of them.
Another thing that, I know myself and others have done is, you know, when you get a couple of advisories in a row, it gets you thinking about, like, like, hey.
can I just find these myself? And the answer is yes, you can find these yourself. So, like, you can wait for some other person to run… use these agentic tools to discover these advisories.
But often, if you just run the tools yourself, you can find a pretty good catalog of issues, and you can, you know, you can fix them preemptively. So, if you have the time and the tokens, consider doing that. I know I did that against Java, and I found a number of… there were small issues, some logical.
some arguably, you know, security-related. There's always kind of a gray area. So, you know, I recommend doing that preemptively, because it's a lot simpler to, you know, solve a problem when you're not under a time crunch, when you discover it yourself.
I'm trying to think if there's anything else, that's worth talking about on this topic.
I think that's all that I had in mind. Yeah, so monitor your advisories, you know, review the documents from SIG Security to figure out what the responsibilities are of you, a maintainer, and, you know, consider doing preemptive scanning of the repos that you're a maintainer for.
Carlos Alberto Cortez 00:08:38 Wait, thank you for that. Ricardo. Ricardo, yeah.
Riccardo Magliocchetti 00:08:41 Yeah, like, I have a question, like, in Python, we have a… huge number of, I think, Security Advisory is, reported by Defenderbot, mostly, or the one, like, including GitHub.
What are about our, instrumentation dependencies?
So, like, in our cell, we test for a very old version of, library screen instrument.
And so, like, does this policy apply to these issues as well, or… Not.
Jack Berg 00:09:20 So, I think it's on, there's… there's some kind of rules of thumb, but it's a little bit on a case-by-case basis. You know, the degree to which you need to, React and publish your own advisory for a problem in a dependency.
I recommend going and reading SIG Security, and if you… the documents from SIG Security, and if you see anything in there that is, lacking in information, open an issue, and we can have a discussion, because if we can take this, like, whatever the conclusions are, and in, you know, inform everybody and get everybody sort of, like, marching in the same direction on them, and reacting in the same way, then that's… that's a good thing. So, Trask, I saw you one… one off mute, so, please jump in.
Trask Stalnaker 00:10:12 My face looks like I want to say something.
Jack Berg 00:10:14 Your face looks like you want to say something.
Trask Stalnaker 00:10:17 I think Ricardo's question was slightly different, kind of specific to when, instrumentations, you often test against old versions of libraries intentionally as a, like, compatibility test. And so, kind of the question there is.
Ricardo, I… I'm curious what… I know in… In the Java instrumentation repo, we do that a lot. We test against really old versions, but… I don't know if… Oh, I do know why, because in our renovate configuration, we've essentially disabled the whole instrumentation tree, The key… the real key from non-automation perspective is whether you ship an artifact with that dependency.
Like, so if a user would get… pulls in our… Artifact, and we transitively pull in an older, vulnerable dependency, then we are responsible.
But ideally, instrumentation… at least, like, in Java terms, we have a compile-only dependency against the libraries, so that, it's not a real transitive dependency.
Carlos Alberto Cortez 00:11:50 Doug?
Jack Berg 00:11:53 So I have one more comment that I wanted to say, but I forgot, and I was typing it into this summary section here in the notes, and that is.
We've had a couple of cases where an advisory is reported against one language, and it has actually affected several languages, or many, most of the languages in some cases. So just, like, be on guard for that. So, if you're a language maintainer, an advisory is reported against your repository, you know, just consider whether this is sort of a structural spec issue that is likely to affect other languages, and if so.
loop in the TC, loop in other maintainers in a responsible way. I'd say actually lean in on looping in the TC so we can do responsible disclosure and we can manage that. But yeah, just, You know, rather than letting the same advisory be opened against many repos, if we can fix it, you know, all at one time, that's preferable.
Carlos Alberto Cortez 00:12:49 Let's try to grab this, discussion. So, Jack, sorry, Robert.
One last intervention.
Pellared 00:12:59 I just want to ask one thing, because as far as I remember, the PC has a rotation for the responsible for handling the CVEs, and I want to just make… if there's a… if is it true, is there a place to know who is this person?
To just not, you know, spam OTC, etc.
Jack Berg 00:13:21 There is a place, I'm not sure if the document is public. If it's not, we should make it public.
Carlos Alberto Cortez 00:13:27 notes, yeah.
Armin (Dynatrace) 00:13:27 And we should also figure out if we want the first responder to stay assigned to the CVE and continue maintaining that one, or whether we want to rotate the duty for existing ones as well each week.
Jack Berg 00:13:45 Harmon, let's take that to the TC meeting in the interest of time.
Armin (Dynatrace) 00:13:48 Yeah.
Jack Berg 00:13:48 Especially because we don't necessarily have the permissions for the original assignee to continue working on it.
Armin (Dynatrace) 00:13:55 Yeah, let's discuss it down. Sounds good.
Jack Berg 00:13:57 Okay.
Josh Suereth 00:13:57 But, by the way, I'm happy to make the spreadsheet public, but we should also possibly move it to… just move the whole infrastructure somewhere public. I'm fine with that, too.
Jack Berg 00:14:06 Right.
Carlos Alberto Cortez 00:14:09 Okay, Nikola.
Nikola Grcevski @ Grafana / OpenTelemetry 00:14:12 Yeah, I was just, wanted to see if there's an opportunity for us to share, prompts or, strategies for using the AI tools for cell scanning, or the preemptive scanning, as Jack mentioned.
I, I think… I mean, I don't know if any of you, we're certainly from Grafana, we don't have access to Methos.
And I have, limited access, which didn't work when I tried it for codecs, security.
However, given that some, I believe, there were some, scans done, Tyler, spawn for, from OTEL as well, using the codec security.
So certain vulnerabilities that were found there, we were able to replicate them using standard, AI coding models, and any pretty much work.
The trick is to prompt it correctly, and… To send chunks of the source code, to it for analysis, and it… it does fine well.
the vulnerability. So, it's a… it's a valid strategy. However, we have to prompt it.
In a particular way to be able to do this. So I just wanted to see if there's anyone who wants to share that, and… Kind of.
I'll start this. I didn't realize, Jack, you were actually doing it, too.
Jack Berg 00:15:31 I know several people are.
I don't know of any forum where we've shared strategies on this type of thing. SIG security could be a good place, because there's always the risk that if you share the strategy, and the strategy can help attackers, that, you know, you're kind of doing a disservice to people who haven't been able to execute that strategy yet. So, let's have conversations about it, and just sort of work through this.
Maybe SIG Security could be a good place to talk about those strategies.
Not the SIG itself, but the repository.
Carlos Alberto Cortez 00:16:04 Correct.
Nikola Grcevski @ Grafana / OpenTelemetry 00:16:05 Perfect.
Jack Berg 00:16:07 As we wrap up this topic, so there's 20 minutes on the agenda for Nikola for an OBI project update. I see you're here, thanks for coming. There's also 20 minutes allocated to stable by default. We have 45 minutes left total.
how do we want to tackle this? There's more topics than there are time.
Carlos Alberto Cortez 00:16:26 Yeah, Lyudmila, I don't know if there… is there any chance that, you can decrease that?
Liudmila Molkova 00:16:33 Yeah, I think we can cut it, cut the stable by default.
shorter, but I'd like to talk about the… some of the parts of it. So maybe we can give it 10 minutes?
Carlos Alberto Cortez 00:16:45 Okay.
That could be a nice one.
Liudmila Molkova 00:16:48 Yeah, thank you.
Carlos Alberto Cortez 00:16:49 Okay, in that case, let's jump and, yeah.
Also, for people coming up, sorry, who have the next topics, please, consider, Not… don't make it shorter than it has to, but consider that. Okay, Nicola, do you want me to share, or do you want to share yourself?
Nikola Grcevski @ Grafana / OpenTelemetry 00:17:06 Yeah, you can share that link I sent. I'm just gonna talk over that. Just keep a project update since we, donated the project and has them going. I have to say, personally, from my side, I did not expect to be this good. I didn't know what to expect when the project was first donated, but it's been really positive.
We've had a lot of contribution from multiple companies on the project, and development has accelerated.
So it's… it's been a great experience.
We're trying to get to a… release Canada this year, or stabilized to a point where this can be shipped as a 1.0, That's what we've committed.
And, maybe I can go over a little bit around what is required for this to actually, from our perspective, to make sure that it's stable and it can be shipped as one out.
One main… main kind of, task that needs to complete, which is in progress, bit by Tyler.
is to actually get declarative config, part of the, part of our config, so… which was sort of grown out of.
a really small config file to keep on adding options, and as you can imagine, is really hairy at the moment. So, Tyler is working on completely revamping our configuration, to be supported, So we call it Pacific 2.0.
And this config. 2.0 will, use the declarative config, approach.
As the rest of the hotel is, converging towards.
As well as it's meant to be, in a way, used to be able to embed OB as part of the collector as well. So, we're thinking about standalone config, standalone tool.
And, but also being a part of how does this fit within the hotel, collector, config, and so on. So… We believe we can finish this year, and that's sort of the major sort of item that will drive whatever we stabilize on.
Apart from that, we're working heavily on stabilization and the security, kind of review and vulnerabilities discovered, and patching those as part of that. A lot of those things that were found were crashes, so… or potential crashes if malformed particular requests get sent, or things that we didn't expect. So… So stability is also a focus, for the next, I guess, 6 months, to make sure we are… Stable and deliver on the features.
From project to project integration, we completed the work to have a prototype for… or not prototype, actually a fully working solution. You can build your own tool collector yourself, so we have the integration finished.
With Obi. It's part of our repo, it's not fully, done at the, collector, because, How we build, and… Essentially, there's certain binaries related to ePPF that need to be packaged into the… Into the executable when it's built, so we're working out those kinks, but that's sort of… On its way.
interfacing with other projects, we have, started to work to connect, with the hotel profiler, so that's driven by Mattia and Florian, I believe, who's on this call, to make sure that we share context for the profiler to pick up traces. So, trace… Profile correlation should work out of the box, and especially… it would be a great combination once both tools are actually built into the auto collector as receiver.
So, that's on its way. I believe the work in OB is done. We are slowly making improvements where we've missed, for example, recently there was a PR for fixing certain things related to Python async I.O.
Wasn't properly establishing the map, so those are small bug fixes, but we should have, for a majority of programming languages.
Support for the profiler.
And… Apart from these sort of integration and long-standing items to stabilize and get to a 1L release, there's been a lot of work.
This happened on new specs or new innovation.
Related to, Eater adding new capabilities.
So, since we've donated the project, we've expanded significantly the protocol support.
I can't name, I think there is an item in there.
About the protocols, if you go back to the previous slide, it's the previous page.
There is additional protocol support. You can see in there, there's been a lot of So, I think we can tick off Nats.
And so there have been a lot of things added since, and we're trying to get to the… sort of whatever people use. There's always a new protocol that we don't support, but at the end of the day, we should try to expand this as much as possible. Recent addition has been a lot of interest, especially from a, I believe, maintainer on the Go Compile Time Instrumentation, Xia Bing, Kai Bing, I… I'll mispronounce his name, who's been really interested in JNAi, so that's one of the recent petitions.
Obi supports Chain AI, the spec out of the box right now for many things. So these are a couple of listed here, but since then, we've added Bedrock, I believe Vertex, and others.
So, this is growing lists as well.
there's MCP support now, things like that. So we're trying to work out through the spec and implement as much as possible. We believe this is particularly important because, of the lack of instrumentation, from any other SDKs related to the GenAI spec, so it will be a good way for OTEL to get the spec to be actually established and, And work regardless of, whether it is the case.
supported or not, so… and this leads me to the next item that we also plan to do, more often this year. So, OB right now does work together with, hotel instrumentations that are Like SDK-based, or agent-based, or something like that.
So that's epic number 4.
We'd like to do more of that, so, get better at figuring out… If an SDK cannot support certain things, for example, does not support Gem AI, that all we can fill in the gap.
And if it does support it, then we can just turn it off. More of that, we've done a little bit, so, making the labeling consistent.
And so on.
But we want to see if we can actually simply run as OB as a base when you can, and then… get better signals with the Auto SDKs on top, especially when it comes down to traces.
Yeah, apart from that, one I think I… actually, an item that might be of interest, to the broader community here is that OBNow does support automatic trace law correlation.
And it should work.
At least we have to try it, even if the SDKs do not support it.
This is purely eBPF, so in a sense, if you have, maybe, like, a Python application, and there is no trace log correlation with the Python SDK, but you're generating traces, and you're writing logs to state it out.
But we should be able to… do the work to correlate those traces and logs. So, inject automatically a trace ID into the log file. This is something experimental, it was recently added to the To the project, so we're looking to test it a bit more, and especially how it works at scale, but, it does work for a couple of, languages that we've tried it out with.
And instead, it uses the same… approach has… or similar logic internally to the trace profile correlation. So it's based on the same infrastructure, just, we sort of override the logs of the target application with additional trace ID. So, Yeah, the rest of the smaller items are in here, Things we're kind of actively working on.
yeah, I'm open to any questions if… I don't know, it's my first time sharing this, with others, but, It's, yeah, just wanted to know if you… anybody has any questions related to the project.
Oh, I should also mention one other thing. We recently added support for Weaver, at least for one spec, I think it's MongoDB. We plan to add more of that, so as part of our Bill process right now.
filing.
And it's part of their tests, so… We were as included, trying to make sure that we're up to the latest spec. Like I said, there's a long wait for us to go there, but at least we've done the work to add one API proof of concept.
I'm sorry, one sec, one sec.
Ted Young 00:27:18 I've got a question for you. I mean, I'm a big Obi fan, and, you know, I'm a big supporter of this project, but I feel like sometimes hearing about, recreating, other parts of the stack that we already have, is there, like, a danger of Obi becoming something of a kitchen sink?
Where it's just got, like, too many things going on in it, and, you know, too many ways to… depending on how you install something, like, what kind of instrumentation you get might be different.
Nikola Grcevski @ Grafana / OpenTelemetry 00:27:52 Yeah, I mean, it's true. It's supposed to instrument everything, and there's a danger with that. You instrument everything, but you don't get the, The results you want.
I think it… my strategy there is that… if you can't run the SDKs, and instrument of SDKs, that should be your first choice. If you can't, then you should use Folby as a pullback. And I believe that with integration with the SDK work, we can achieve that, sort of, automatically. So you run this at the base.
And maybe doesn't have all the details, and it cannot for certain programming languages, especially.
As long as it works great with the SDKs, I think we… It should… I don't know if that answers your question, but I think that's what we want to get to.
Kind of an add-on rather than a kitchen sink replacement for everything.
Ted Young 00:28:49 I think it's, to some degree, like, motivation for us to, with the injector and other things, to get the SDKs.
Like, the longer there's a gap in installation there, right, there's gonna be more pressure on Obi to fill that gap, so it's more like motivation for us to finish some of that other work.
Nikola Grcevski @ Grafana / OpenTelemetry 00:29:09 I agree, yeah. And if you inject with the SDKs, and let's say there's no trace-law correlation, likely to do the rest of the work, and then sort of integrate with that without you having to do anything.
Until the SDK provides trace mode correlation, and then it will start.
Carlos Alberto Cortez 00:29:29 you know?
Liudmila Molkova 00:29:31 It's less of a question and more of a pitch.
How many HTTP client instrumentations we have around total, maybe 100 in total, or some order of magnitude.
Does it help anyone that we have 100 different HTTP-clad instrumentations? No. What if we could have one, maybe VF-based hobby, and maybe a few that are specific in some edge cases?
And the… the pitch is here. Can we make Obi work together with SDK? Because I think now they are mutually exclusive. Can we support telemetry that's… cannot come from Obi and SDKs?
And kind of embrace that topic provides the, network layer for everything as a default.
Michele Mancioppi 00:30:16 I actually could… I could comment on this one.
There are tons of scenarios where you cannot run eBPF.
you're not going to run a BPF on Lambda, or it's not until some stuff changes in the Lambda runtime. Serverless scenarios are very, very difficult, and depends very much on the platform.
you will still need to be able to instrument 40 different Java HTTP clients to be able to cover the platforms where the user deploying the instrumentation doesn't have control of the Linux kernel underneath.
Nikola Grcevski @ Grafana / OpenTelemetry 00:30:53 Yeah, that's true. So, I mean, if it's not possible, OB is not possible, so you need the rest of the instrumentations to work, and sometimes those instrumentations do provide, higher quality information, However, I'm going to say for, for other things, I believe Florian started this work recently into the OB project of using some of the SDK-provided information That metadata that the profiler intends to use as well.
And we should be able to get more detailed information about what the SDK is actually doing. Right now, what we do is quite simplistic. We detect if there's SDK metrics exported, or SDK traces exported, and then we disable our metrics or traces exporters based on… for that particular application. So, you can run over it in the background, and you can have, SD instrument identification, some sending traces, some sending metrics, so we're filling that gap.
However, that's not, sort of, enough. When you think about perhaps there's GenAI workload here, but the SDK does not support GenAI for this particular language. It would be nice if we can convert those and produce those metrics. So, with this work by Florian, I believe we'll get to a point where the SDK can tell us what they don't do, or what they do, and we'll be able to fill in the rest.
Josh Suereth 00:32:23 So I think I might have been next. I have, I have two things. One is a statement, one is a question. The statement is, I used your builder, by the way, and thank you for making that, because it makes it really easy to kind of build and test and work with us. So, really excited to see that land.
yeah, compiling eBPF, natively was exciting. Anyway, the other statement was, or the other question, because it goes into this, as you build this, like, the work Florian's doing is kind of like a level of communication. My intuition here is that we need to figure out how to build a cooperative SDK with eBPF.
And the way that we do that and the things that we need, the more that you come back to this group and say, hey, if we could figure out a way to solve problem X of, like.
this kind of a communication or whatever. I don't know how bidirectional works with EVPF, because as far as I understand it, it's one-directional, but if we can figure out a way to do some communication here.
to do more cooperative natures. That's… that's the thing I'm really looking for, and that's something I'm super excited about, like, because if there's an SDK, you know, OB does less, great, but, can we do more if we have Obi, too? You know, like… like, what… what are the… what do you need from the spec to make that easier to deal with? And are there things we can do to make OB easier to write to begin with?
I agree with, what McKelly was saying, where you know, we can't use eBPF everywhere, and eBPF's not necessarily the same on Windows as it is in Linux.
But, I still think that there's a lot of power in what we do here, and thinking about these, you know, remote inspection use cases when we design APIs is something we need to kind of account for. So, whatever you can bring to us, like, I don't know what you're working on now besides… what Florian's working on, but I see that being a potential area for us to invest in after your 1.0.
Nikola Grcevski @ Grafana / OpenTelemetry 00:34:17 Yeah, okay, that's… that's a really good point. We haven't thought too much about it, around… I mean, we've thought about how to make sure we work great out of the box with the SDKs, or with agents, or everything that's installed, at least not duplicate telemetry, things like that. One thing that's come up recently has been Ob can maybe pull out information such as DNS or network-level data that's may be interesting to certain people. They'd like to see, like, how many network requests did you make to make… finish this, particular request, so there's definitely interest for, enriching the information from eBPF, what eBPF is great at.
And yeah, thanks for that open door. I don't know off the top of my head what we could ask for now, but I'll… yeah, I'll bring it back to the SIG, and thanks for that.
Carlos Alberto Cortez 00:35:12 By the way, we have… we are almost in the 10 minutes, so, Jack and then Robert, yeah.
Jack Berg 00:35:17 I'll be quick, yeah, I just want to echo what Joss said. I would love it if, OBI could have some sort of foothold in the specification, and just a place where we could describe things like what the purpose is, what the scope is of the project, and how it interacts with SDKs. And so, as we sort of, you know, add additional details about, like, how these things communicate, you know, when OBI does something, when SDKs do something, we can just write that down.
And, you know, I think that has a number of benefits, including raising the visibility of OBI and making all the expectations explicit about how SDKs interact with it. So, That's all.
Nikola Grcevski @ Grafana / OpenTelemetry 00:35:58 Thanks.
Pellared 00:36:00 So regarding this interoperability between OBI and SDKs, I think we already have a precedence in OTEP. I initially thought it was for OB, but I think it was for the EVP profiler.
Where we have, I think, some OTEP which says that some part of the memory can be written that OBI… defines some part of the memory that the OBI can read.
I think the use case, which is in the OTAP, was to use the same resource model, so that if the profiler and the SDKs are sending the resources in their telemetry, they're sending the same data. So, I think the same model could be used by OB.
If it works. That's all from my side.
Carlos Alberto Cortez 00:36:49 Okay, if there's nothing else on the topic, thank you so much, Nicola, for the presentation. Thank you. Yeah.
Sweet.
Let's keep discussing that offline. Okay, and let's move on for the sake of time. Robert, you have a pair of items there.
Pellared 00:37:05 Yeah, let's go fast. So, first of all, I created an issue and wanted to, like, advertise it here to catch as many proposals and comments as possible. So, in AutelGo, I think we, I think David and Tyler can confirm this is correct. We added GitHub Copilot instructions.
and we saw a lot of improvements how much the co-pilot has been catching issues. I think it's right now a better reviewer than myself, and I thought that for the specification level, a lot of stuff can be also better handled by co-pilot than by humans. Like, if stuff is, like.
not clear, stuff is not consistent with other parts, and things like that. Also, we have a lot of guidance which… and stuff which we already probably forget about it, so I just want to create a PR proposal for co-pilot, for Copilot instructions, but beforehand, I just want to catch as many, like, thoughts. Maybe you can even call out here things that you're looking at when you're making code reviews, which are even not mentioned anywhere.
So anything that you think is good, that the co-pilot can just put comments here and upvote stuff which you think is really important, because I think there's, like, a limit for Copilot, that it can be, like, only A few thousand characters.
And it's not a good practice to link other documentation, because the context will… yeah, I have read some things about it, so probably it should be self-sustained, the document. You should not refer to other places if possible.
So yeah, that's all from my side, and maybe let's just… go further.
So…
Carlos Alberto Cortez 00:38:43 Yeah, yeah, yeah, let's hope that, comments come offline. Exactly.
Pellared 00:38:52 So, here are two PRs related to each other. So, this is the first one which I recreated. So, when we did non-OTLP, non-OTLP representation of any value, which is used for things like ProVTUs, maybe… maybe it was also used for Jaeger zip, which is right now kind of deprecated, or maybe even removed.
The thing which, so, in AutelGo, we use this non-OTLP representation.
In the kind of two-string or, like, string representation, also for debugging in tests, etc.
the Prometheus Exporter uses as well.
And the thing which was… which is missing, at least right now, at least for us in debugging, for debugging purposes, is the representation of a single attribute.
So, this only expands this non-OTLP recommendation, just to define how to emit something which just wants one attribute.
We do not see any use case for non-OTLP exporters that meet a single attribute, but they may be things like that, so this just tries to expand on this one.
I saw that Bogdan, which is unfortunate here, had also some comments regarding the representation, which is stable right now. Bogdan was asking, maybe we should… maybe that the representation is not good, maybe it should be the representation which is used for OTLP JSON, and here's why we have not done it.
I think it's a valid concern, but I think it should be a separate issue. I checked that the current spec regarding the non-ATLP representation, I think most of it was stabilized in January, and I think there's a pretty high or non-zero chance that stuff which is stabilized has not been implemented. We could revise it and consider it as a bad fix, but also, I think these are separate concerns. If the representation is correct, this one, this PR just follows up with the current, current guidelines, or maybe current, way we have been stabilizing, but if we want to change the representation, it's a separate issue. Maybe, I don't know, maybe the TC had some, I don't know, or had some thoughts about it.
I don't know, maybe it's… I remember that Facebook created the original PR, I don't know, any comments here, or… yeah.
That's all from my side.
Do you run?
Tigran Najaryan 00:41:29 So, Robert, we do the strings, or we, at least, I think, allow the strings in OTLP as well, right?
For the… for the same reason.
For the numbers.
Pellared 00:41:39 Yep.
Tigran Najaryan 00:41:39 there is a… there's a definition of JSON format for OTLP, and I think we say there that we want to use the strings.
So probably we should just do the same thing here.
Pellared 00:41:51 Yeah, so the.
Tigran Najaryan 00:41:52 If I remember correctly.
Pellared 00:41:53 Yeah, so the problem is that I not opposed it, but I think it's a separate PR, so we do it, you know, in two places, because this is just, you know… and the second problem is if it's backwards compatible.
Making the string as numbers… as strings and not numbers.
Numbers as strings, not as piece of numbers.
Because if someone has already, you know, implemented it, I'm not sure if it's, compliant. Like, for instance, for the Prometheus exporter, things like that.
Tigran Najaryan 00:42:27 Okay, I had a question also. This is only about attributes. For debugging purposes, if I want to look at some other telemetry data.
Are we defining this just for the attributes? Because we think that's what you need for debugging purposes most often?
Is that the thinking here?
Pellared 00:42:46 Currently, yes, but I just won't… yep.
Trask Stalnaker 00:42:51 Yeah, maybe that's kind of what my question also is. Is this affecting… It seems like you're… making this for the non-OTLP scenarios, like the Zipkins and Prometheus's.
And in those cases, sending them as strings seems weird to me.
Pellared 00:43:11 Yep.
Tigran Najaryan 00:43:17 I'm just trying to understand where this is leading us. Is this just some sort of a… limited effort to just be able to debug the attributes easily when you don't have OTLP somewhere.
Or you're going to continue this and make into a full-blown… Debugging representation for all of the telemetry data.
That seems to be the logical continuation of what you're starting.
And I'm not sure we want to do that, because if… If that's the goal, then… Maybe we just use OTLP as the debugging representation, or TLP JSON.
instead of Coming up with a new format.
Michele Mancioppi 00:44:02 I.
Tigran Najaryan 00:44:03 specific Venice…
Pellared 00:44:05 Right?
Tigran Najaryan 00:44:05 a different format, because it's simpler? Is that what you're aiming for?
Pellared 00:44:10 So, right now, we are using this ELP representation for the bugging purposes, not will go. Like, I think that, you know, for the bugging, I think the… The corner cases, when you do not know what words, the attribute type, etc, these are only the corner cases.
And people who are usually debugging know what are the types, what they're being represented. So, the lostness, you know, the kind of loss of information.
I think it's not important when you are just debugging. And I… personally, for me, it will be just a bloat. If I'll be reading and have so much information for each attribute, the type, if I see, like, if I see, like, 99%, like, in most, like, I think for all the cases, when I'm debugging something, I will know what is the type.
Tigran Najaryan 00:45:00 I may be misunderstanding something here, but for the sake of time, I'll take a look at it offline.
Pellared 00:45:06 Okay, the question is, because here I'm just trying to, you know, I just used the non-neo TLP, I think we can consider removing the bugging part from my proposal, so just to not be that much… I don't know, because I think this is the first time I put in the spec that it can be in the bugging context, so maybe I just remove this debugging context, and just say… let's say that just for non-MTLP representation, and it might be our autogo decision that we use it for… for debugging purposes.
I will make a suggestion in the PR.
Carlos Alberto Cortez 00:45:44 I saw the Mikael Ju, yeah.
Okay, let's continue that offline, I guess.
Pellared 00:45:50 Yep, thank you.
Carlos Alberto Cortez 00:45:54 Okay, yeah, then, we have, Bradon.
year-round.
Dmitrii Anoshin 00:46:01 Brandon isn't here, but I can speak about this issue.
So, I… I'm coming from a system semi-convention, working group, and we are running into a problem when we… where we cannot deliver enough information about a particular time window pre-aggregated metric. And, for example, for some metric, like CPU load average, we put it as a… part of the metric name. For some of them, for some other metrics, like CPU… CPU utilization, for example, it can be implicitly.
taken from the interval of the data being reported, but for some metric, for example, there is metric CPU usage that we take from Kubelet API, and that one already pre-aggregated over… Completely separate window.
And we, like, there's nothing we can do, and we just send it as is, and that… detail about window pre-aggregation is actually not even available to the user until they look on implementation details of Keyload API. So, we are suggesting to add another field to metric protocol for OTLP that would, pass that information, that field, that would show, aggregation window, for aggregated metric. And, we are looking for opinions, from, from the spec, From… about that, if that's a good idea.
Carlos Alberto Cortez 00:47:44 So, I think we will not have time to discuss that here, because we want to talk about this by stable, but if that's okay, just please, people who are, you know, versing metrics, please comment on that one. I don't see much feedback, so we really need more eyes on this one.
Tigran Najaryan 00:47:59 Did you consider the metadata field? We already have an arbitrary key-value list there, which is called metadata in the metric.
Dmitrii Anoshin 00:48:09 Yeah, potentially we can use that one, but we still, like, define some kind of a convention around that.
Tigran Najaryan 00:48:16 Yeah, give me the SENCOM for that, yes, yeah.
Dmitrii Anoshin 00:48:18 Yes, yes. And that's the way to go. I haven't even ever saw any usage of that field.
Do… Excuse me.
Jack Berg 00:48:30 For exactly one thing right now, to represent, you know, information that would be lost in the Prometheus to, to OTLP translation, because there's Prometheus metrics types which aren't completely representable as open telemetry, so it facilitates lossless translation, or round-trip translation.
Dmitrii Anoshin 00:48:50 Okay.
In that case, potentially, yes, we can use that.
So anyway.
Tigran Najaryan 00:48:56 Yeah, the definition seems to fit what you need there. It says additional metadata attributes that describe the metric, which seems like a very good fit for what you need here.
Dmitrii Anoshin 00:49:07 Okay.
Yeah, and it'll be maybe a bit more data over the wire, rather than have another field, but given that it's a pretty niche use case and not that widespread, I guess we can go with that one. Sounds good.
I'll comment on the issue.
With that guidance, unless anyone else has other opinions as well. Thank you.
Carlos Alberto Cortez 00:49:32 Thank you so much for that. We only have 12 minutes, so the next one will me, that's 30 seconds. The context scope is still there. I updated that with the latest feedback. If you're interested, please review that, etc.
Okay, oh, sorry, I totally missed Ricardo. Two minutes. Open a PR for controlling propagation at boundaries.
Riccardo Magliocchetti 00:49:55 Yeah, I'll be really quick.
I even asked about the issue of controlling propagation between boundaries some months ago, and finally was… I was able to open a PR.
I have, like… A prototype in Python.
And so… yeah, if you could take a look… And give me some feedback, we can improve the… the proposal Yeah, maybe get this merged in the future.
So… Thanks.
Carlos Alberto Cortez 00:50:37 Yeah, thank you so much for working on this. Yeah, this is a long-requested thing.
Okay, I think we can, yeah, keep this offline for now. Lydmila.
Liudmila Molkova 00:50:52 Yeah, thank you.
So, we… Had a discussion last week on this table by default, and I wasn't there, so it's my recap of… based on the recording.
Inc.
I think one of the things… we probably cannot go through everything, but one of the things that was discussed is that there is a lot of work there. There is no single driver And the first goal of, if we want to continue the WhatAP as a whole, would be to actually advertise it among maintainers.
Have a campaign, explain where needed, maybe trim down some excessive details that are less of a vision and more of an implementation, move them to some Sub-work streams and so on, but essentially, this side app needs a driver.
Unless we want to break it down into multiple pieces.
And Austin seems to be stepping down a little bit from the hotel, spending more time in other areas. So, probably the most important question, do we have a driver?
Yeah, Dad.
Ted Young 00:52:03 Yeah, I'm… I can take over trying to drive this.
But… I do feel like what we discussed last week was that even though we want to stabilize all of the instrumentation, we simply don't currently have the labor force to do that. Like, the SDK maintainers can't realistically, take over managing all of contribib in most languages.
So, we need to come up with an approach for tackling this.
Specifically for, for updating instrumentation, marking it as stable, and, you know, keeping it up to date.
other aspects…
Liudmila Molkova 00:52:49 With our gear.
Ted Young 00:52:50 Go for it.
Liudmila Molkova 00:52:52 argue that it's not the goal of this ODAP to stabilize everything, right? It's to develop criterias and policies and everything.
And stabilize some parts in the right way, and let others Follow.
Ted Young 00:53:10 Yeah, but it seems… but who… who are the others? Right? So that… that to me seems like… like something to… it's not an ultimate blocker, but I think we need to… in a fundamental way, revisit how we're going to manage this instrumentation. We have tools we've been working on, like Weaver, that can help.
I think Weaver could be then successfully used to really constrain AI coding tools, to kind of help us keep these things up to date, but I think we need to have some people trying to experiment and come up with, like, an approach to lower the cost… lower the maintenance cost on these things, rather than hoping that we massively increase the number of, like, consistent contrib maintainers who are, like, definitely going to be, like, responding to, like, PRs and issues.
So, I think we should go around and talk to everyone about that, but that was kind of my interpretation as, like, the core blocker.
Other parts of it, I think we can… Use our regular process, but that… that's, like, a pretty big chunk of getting things stable, is the instrumentation.
Liudmila Molkova 00:54:25 Right, so, do… do we think that the work streams we have there, like, represent this reasonably well? Because none of them actually talks about instrumentations. Or is it the distribution and component definitions?
Ted Young 00:54:43 Well, if we don't have the ability in the short term to, Go through and mark a whole bunch of instrumentation as stable.
Then, coming up with, say, stable packaging and things like that.
Is kind of a non-starter, because you would get very little instrumentation.
Stabilizing other parts of OpenTelemetry, like the collector and things like that, I think we have… we can handle. But it's around, like, packaging up instrumentation in the SDKs. That was the one part where I think we need to… to come up with a more comprehensive plan.
But I'm happy to socialize this with, you know, SDK maintainers and things like that.
Jack?
Jack Berg 00:55:32 I think part of the, the… and I've said this in a number of forms, but part of the… the worry about stabilizing things is that it seems like a huge effort, because, like, implicit in the statement, we want to stabilize something, is this, this fear that we… you have to… you have to support that thing forever in its current form. So you want to make sure it's really right.
But we need to change our thinking around this. Like, stable by default means stabilize things as they are, and come up with a regular cadence for bundling breaking changes.
Right? So, like, if you're… if you have a distribution of instrumentations that bundles together 20, 50, 100 instrumentations.
Some of them are in really good shape, some of them are in questionable shape. You're still gonna publish a major version for that thing.
And you… what you… what we want to be able to communicate, at least in my opinion, is that the… the people who curate these distributions should come up with a cadence by which they expect to publish the next major version.
And in between now and the next major version, they shouldn't break the instrumentation.
And when they… and they should bundle together the breaking changes, you know, together into their next major version. And we can come up with standards for, like, you know, things like, hey, if you have major version 1 and major version 2 is coming.
15 months from now, you know, when you publish Major Version 2, how long do you support Major Version 1 for, right?
So, I… that's kind of where my head is at on this, like, we need to kind of de… Make stabilizing instrumentation a less stable thing by giving ourselves the ability, the permission, to make breaking changes on an ongoing basis, but in a structured manner.
Ted Young 00:57:23 Yeah, and I think just we… what I was surprised by, and it was very good feedback, was just that we hit an even earlier wall, which is, like, what we would like to do as the first version of this is not even update existing instrumentation, but say, hey.
If instrumentation is out there already in a de facto state, where it's been in production for a while, it's not, you know, no one's reporting bugs on it, it seems fine, the instrumentation, you know, the semantic conventions might be out of date or something like that, but there's no reason to consider avoiding running this in production. Let's just mark those things as 1.0. And then, like you're saying, Jack, like, if we come back in later and update the semantic conventions to the latest stable version, we'd want to issue a 2.0 and have some process for, you know, bundling those changes and supporting the 1.0. But we immediately got concern and pushback from some SDK maintainers saying, just.
Who is it that would be marking these things as 1.0? Because it seems like whoever's doing that is saying they're on the hook.
for responding to bugs and problems and things in that repo. And the SDK maintainers don't necessarily want to be those people because they don't feel like they have the capacity. So even just doing the simple act of marking things that are perceived as de facto stable as 1.0 was getting some concerns. So I think trying to, like, figure our way around that first issue is something we have to put some effort into. Because it seems like even a blocker to getting to the concerns you are having, if I'm interpreting people right.
Does that make sense?
Liudmila Molkova 00:59:07 I've just… We have just a minute, maybe Tigran can share her thoughts.
Ted Young 00:59:13 Yep.
Tigran Najaryan 00:59:13 Just very quickly, I agree with Jack, we need to have an appetite for new major versions, nothing wrong with that.
There is one area where we need to be very careful with, which is we should continue supporting old APIs for a very long time.
SDKs and instrumentations, I'm fine with having new major versions periodically, but if someone wrote code against OTL API, that code should continue working for many years without needing to change it. That's the only area where we can't obsolete stuff and stop supporting. That can't happen, because we want that code We want to encourage people to write against Autel API, and the way to encourage it is to make sure people feel safe that whatever they write today is not going to be broken in a month or in a six months from now.
That's all I wanted to say.
Ted Young 01:00:11 Completely agree. And it does seem like we're good at that part. And that's also the part that SDK maintainers are fine.
paying attention to and putting effort into. It's just figuring out how Like, almost figuring out the ownership model for instrumentation needs to get updated.
Going from, like, the community manages it, and they do with it what they will, and that's why it's in Contrib, to, like.
we collectively care about this instrumentation, because OpenTelemetry doesn't do anything useful, unless there's at least a subset of this instrumentation that's in good working order.
But figuring out where to get the people for that, or how do we reduce the cost of doing that, I think we need to get creative.
On that part.
That was my interpretation, but I want to get more feedback from maintainers, so definitely reach out to me, if you're a maintainer and hearing this. I would love to hear your thoughts, and I'll be reaching out to you as well.
Liudmila Molkova 01:01:14 Cool, so then we're at time. We will follow up on this. Ted, you would be reaching out to maintainers. I think we need to document the stability policy we've been talking about from different aspects as well.
Jack Berg 01:01:27 That's a material thing we can take an action item on, is starting to, like, open a PR to the specification to make this concrete, to differentiate between the classes of components, and to sort of get people socializing, get people comfortable with the idea that major versions are part of the deal, especially with the instrumentation.
Ted Young 01:01:46 We have some of that in the spec right now, but it's super, super ancient. We could look at updating that stuff to add a lot more clarity.
Liudmila Molkova 01:01:58 Dean, thank you all.
Jack Berg 01:02:00 Take care.
Carlos Alberto Cortez 01:02:01 Thank you so much.
Stay safe. Ciao.
