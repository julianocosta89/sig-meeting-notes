SIG: Profiling WG
Date: 2026-05-28
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Felix Geisendörfer** 04:58 Right. Hello and welcome, everybody. We're about 5 minutes in, so let's get started.
I'm gonna share my screen… Alright, can you see the Google Doc?
**Ivo Anjo** 05:21 Yep.
**Felix Geisendörfer** 05:21 Okay, well, thanks, Evo. Okay, as usual, we can start with action items. I'm gonna… Tried to copy those.
And… Let's go start with the first one.
This is about a discussion upstream on how big OTLP payload sizes should be before they get dropped. The OpenTelemetry Proto Is making recommendations to implementation, such as the collector, but also exporters and clients.
And, yeah, the update there is, I participated in the discussions on behalf of the Sikh, and At some point here, I provided some… some data. Don't know where the link went.
Oh, yeah, sorry, it's GitHub, GitHub doing its GitHub thing, you know? Like, who would want to see the previous discussions? This is, like, not a use case, apparently.
Okay, here's a document, so in case people haven't seen it, so I did an analysis on how big the payloads are we see in one of our staging environments for profiling, and sort of extrapolated this data to a fully loaded host with 64 cores, which We can argue a lot about whether or not that's representative, but I think, like, if we target 64 core machines that are heavily loaded as a default for how much data we want to be willing to accept in one payload, we're not gonna drop a lot in practice. I think it's pretty rare for people to run larger machines with higher loads.
And when they do, I think that's sort of where you get into the big boy league, where you can be expected to tweak default configurations to some degree to make your use cases work. So yeah, I'm not going to go over all the details, but there might be some interesting stuff in here for future discussions on sort of how to optimize the… the protocol for efficiency or, like, things like that, because we're now in alpha phase, so I think evaluating how well we did so far, and if any changes are needed might be… worthy of discussion at some point, but yeah, we're gonna skip this and basically just say this is done now. The outcome of the discussion was that the new limit is 64 megabytes now.
Any… anybody has any questions before we move on, or comments to the next item?
**Florian Lehner** 07:50 Do we want to merge the PR on SIG profiling you opened? I think it's still in draft mode.
I think that's the base for the discussion, right?
**Felix Geisendörfer** 08:00 Yeah, we probably should merge that, so it's just not pending there. Let's look at that one.
Thanks for suggesting that.
Yeah, I guess I should promote it from draft to non-traft, ready for review, Yeah, this PR is essentially just adding some… a Python notebook with analysis. The dataset is uploaded to Google Drive. It would be great if people could check if the Trive data is accessible from this link. I tried to share it with public, but it's always… can be tricky.
And… yeah, I don't think it needs stringent code review, necessarily. Like, if somebody wants to change how the data… one thing I can offer, so, is if somebody wants more data, like, I'm extracting a lot of statistics from the dataset we have, but if somebody wants more data at some point, feel free to send a pull request to the… main.go file here that was used to extract all the properties, and I could rerun the data extraction on real data.
Yeah, I'll drop the link and ask for reviews on this, and yeah, if somebody wants to rubber stamp it as we speak, that's also fine.
**Florian Lehner** 09:18 Yeah, I will just rubber stamp it. I think we have a value in just keeping the tooling around, and can progress on it further if you want to.
**Felix Geisendörfer** 09:29 Sounds good. Yeah, if we get rubber stems, then we can, merge it in right away. It's not load-bearing, so as you can find.
Cool.
Anybody else on this? If not, going once, going twice. Let's move on to the next item. Figure out key value unit proposal.
So… My last recollection, it's been a while, is that we had two proposals on the table, one from Florian that is more principled long-term thinking, and one from myself that is a little bit more short-term, what we could do immediately without, large upstream discussions, and waiting for certain reviewers for, several months again.
I don't… I think on my document, if I recall correctly, I had… there were some comments from Christos, and I think I got back to you, Christos, on some of these. Maybe you could take another look, to conclude those discussions, and then I could do another update on the short-term proposal.
**Christos Kalkanis** 10:33 Yeah, sure.
**Felix Geisendörfer** 10:36 Yeah, I don't have too much other than that. I think we… once we sort of have alignment on those two proposals, we can take this to the, to the upstream… folks and see what resonates there. I don't know, Florian, if you had any new thoughts on this, or…
**Florian Lehner** 10:53 No update on this, I wanted to bring it up at some point with, specifications sake.
But, yeah, at the moment, quite busy, and, didn't have time, and as we don't have a fully agreement on this.
I think we have some time left, but yeah, at some point, we need to move on.
**Felix Geisendörfer** 11:24 Okay, cool. Yeah, Chris, when you get a chance would be awesome, and then… Microphone is falling around, okay. Okay, any, any last thoughts?
**Christos Kalkanis** 11:38 I think before we move on from this, I think Alexi had some input there as well, if I remember correctly in the last minute. She wanted to take a look. I'm not sure if he did. It's been a while since I looked at the documents.
But I think Alexi will join today. He said he's gonna be half an hour late or something, so maybe we can… once he joins, we can set up a.
**Felix Geisendörfer** 11:56 Okay, listen.
Okay, yeah, let, let me do that.
I'll… I'll add an item… well, let me just move this to the bottom of our agenda, so we'll circle back to it.
Just do a little… break here so I remember this.
Thanks. Cool. Any other thoughts? If not… 31's going twice, we move on to Jonathan's, PR for moving original payload to dictionary says done, so I guess… Not sure if you wanna… oh, done, the PR's here, and it's not merged. Is there anything… What's the current status here? I guess there's…
**Jonathan Halliday (IBM)** 12:42 It's not merged, because I marked it, do not merge! It's a breaking change, which is why I didn't want it in straight away. Yeah, I don't think there's anything really to do there.
Does… I think, Some feedback on it, or any, by all means, look at it and give me more feedback if you… You want more changes, but it's… it's pretty straightforward.
I only comment on the existing comments. Somewhere in the documentation for this, we imply that the kind of unit of granularity for the payload is a file.
Which is sort of approximately true, but I could see use cases where, for example, you capture the profile to an in-memory buffer.
you know, just copying that buffer was the unit of payload, in which case it doesn't really have a file name, so I'm… China not loving the idea of making attributes relating to the file name compulsory.
I think the proper phrasing there is probably, if this came from a file, then This semantic convention for… for how we… refer to the, you know, the file name, suffix, file extension, I think it is.
should be used.
But it doesn't make sense to say, you must use these, because there isn't necessarily a file you can use them against.
**Felix Geisendörfer** 14:05 I see. This is in response to this comment from Florian.
**Jonathan Halliday (IBM)** 14:08 Yeah, yeah.
**Felix Geisendörfer** 14:08 Yeah, I would be inclined to agree with that, that we should encourage these attributes to be set when present, but not require them.
**Jonathan Halliday (IBM)** 14:18 Yeah, so I'll do another pass on it at some point and try and clean up the language a bit to communicate that in some clear fashion.
**Felix Geisendörfer** 14:28 Glorian, does it make sense to you, or got any… okay.
**Florian Lehner** 14:32 Yeah, sounds good.
**Felix Geisendörfer** 14:50 Ugh.
Okay, cool.
Updated.
Okay, otherwise, yeah, more feedback, please, to this. Anybody else has more thoughts?
Before we move on… Going once, going twice… Okay?
I suppose Alexei is not here yet, right? So I'm gonna move these to the… When Alexis here section.
open GitHub issue, for including OTLP.
versions and payloads haven't done that yet, partially because I had, like, some discussions, around this, and… It's very likely that a naive proposal will be shut down for various reasons, so I do need to give this a little bit more thought before doing it, but yeah, hadn't had time yet.
Okay, ristas has a few PRs that were in need of review, I suppose they still are.
**Christos Kalkanis** 16:12 I think one of them was merged by Tigran, recently. I think it was the, yeah, 4932, if I'm not mistaken.
**Felix Geisendörfer** 16:21 Yeah, absolutely.
**Christos Kalkanis** 16:21 that's done. The other one has been languishing for a while. It needs one more approval for some of the PC, which apparently, I don't know why it hasn't happened, it's been more than a month, probably more than a month and a half now, but Josh opened the pulley request against OpenTelemetry Proto, basically where he's expanding the set of people who can make Approving decisions.
To cover, essentially, all the providers and maintainers for the auto.
protocols, so that includes us as well. So my guess would be that we can… shown messages as well. Yeah, it's this one.
**Florian Lehner** 17:02 Coming back to the… to the becoming maintainer, approver for AutoProto, it's a decision by the DC that they want to offload work.
And that's why, people that were really active in, the old proto… repository did become part of the auto-proto, approvers. They can approve, but they did not, cannot emerge, We, as Profading, could already, or did already, get a green checkmark when we approved on the proto, because we were a subgroup in somewhere.
Yeah, but now it's just a dedicated, group, so it's not only TC anymore, it's a little bit more wider.
**Christos Kalkanis** 17:49 Okay, yeah, great. So hopefully that will make it easier, or faster to get approvals, and then if we do have to ask someone from ATC to merge this, you know, that's something else. Hopefully that's gonna… it's a lot faster, I would imagine, to ask someone to hit a button than getting an approval.
**Felix Geisendörfer** 18:16 Sorry, this, applies to the proto repo. Also, to the specification repo, or…
**Florian Lehner** 18:22 Just proto. Specification is still with TC.
**Felix Geisendörfer** 18:27 Cut it.
Okay, so… Regardless of that, I think for both of these PRs, you still want more sick refused crystals, is that correct?
**Christos Kalkanis** 18:48 I think I have all the secret reviews I need. It's just for the, the related documentation changes to the proto, that's where I need… someone, yeah, one more, ideally. Like, Alexi has approved it. Jonathan, if you could take a look.
That would be nice, because I'm essentially rewarding paragraphs that you worked on before.
**Felix Geisendörfer** 19:18 Okay, I will, if I get a chance, also try to take a look if… Jonathan doesn't get time to do it.
Okay, and this one, let me just capture here, is blocked on… Proto maintainers merch… merging, right?
**Christos Kalkanis** 19:42 No, it's actually the other way. 4965 is blocked on… it needs an approval from the TC, so Tigran has been asking around… I have asked around, I don't know why we haven't gotten an approval there yet.
So that needs one more TC approval.
It has all the SIG.
Yep.
this one.
**Felix Geisendörfer** 20:05 Okay, okay. Okay, sorry.
Okay.
**Christos Kalkanis** 20:31 Yeah, I can… I can record those, Felix. You can save some time now, we don't have to. Like, I can go… I can go into the agenda.
**Felix Geisendörfer** 20:36 Thank you, thank you, much appreciated.
You can tell I'm rusty because I haven't been to the last meeting, or maybe it was two, because I think we skipped with a holiday.
**Christos Kalkanis** 20:47 You're a lot better at this than any one of us. Some of us have tried.
**Felix Geisendörfer** 20:53 It is, it is, yeah, it's a, it's a acquired taste, a skill set, for sure.
Okay, then next one is revised data form, or sorry, any more on the other two? If not, let's move on. Revised data form and PR to remove redundancy.
**Christos Kalkanis** 21:11 Yeah, this was finished. I did all the changes.
**Felix Geisendörfer** 21:17 Oh, okay, this is the same one that we already had listed, right?
**Christos Kalkanis** 21:20 Yeah, yeah, yeah.
**Felix Geisendörfer** 21:21 duplicate with this one. Okay, I'll take this one out and marks this as done, right?
**Christos Kalkanis** 21:25 Yeah, I've already marketed them, if you look at… yeah.
**Felix Geisendörfer** 21:28 Okay, cool. So I… yeah, I copied, and I think it lost the formatting in this, and… yeah.
I see, I see.
My bad. Okay, then we are… On to another Alexei… Alexei one? I think he's still not here yet, or is he?
Okay, then I think we got through the action items, and once Alexei joins, we can come back to these other items.
And we can check to the regular agenda. So far, we have one agenda item on thread context. If anybody has any other items.
Maybe I can… Propose one just ad hoc right now.
A few better roadmap… If, yeah, but if anybody else comes up with one, we probably have more time today to cover more crowd. Scott, do you want to talk about thread context?
**Scott Gerring** 22:26 Cool. Yes. Good afternoon, everyone. Not much to say here, really. We're trying to solicit a bit more feedback on the PR, so we can push it forward. We got a fair bit already, we've iterated over it, we have one approval.
That seems rather serious to my mind, and I think it would be good to get some feedback from this group in particular. Florian, I know you've been looking at it. I'm not targeting you in particular, but I value yours in particular as well.
**Florian Lehner** 22:53 Yeah, I will look again. I think your comment makes sense to not have it as attributes. I think we should just be more explicit about naming it in the OTEP, that we see the benefit of not using the attributes, because using the memory directly is fast in this context of sharing the thread-level information. I might have missed this, but I didn't have time coming back at the moment on the move.
**Scott Gerring** 23:22 Yeah, and a bit of a call-out back to Felix's comment at the start of the meeting, it's so hard to work out what has happened in discussions all weeks ago in GitHub PR feedback. It took me a while to dig out that thread to point you at it.
But, thanks.
**Felix Geisendörfer** 23:37 Yeah, if I didn't know it any better, I would say GitHub is designed to actually avoid collaboration. I don't know how that's possible, but…
**Ivo Anjo** 23:44 To be fair, someone pointed me to this button the other day, and I have kind of experimented with it a bit, so yeah, give it a try.
**Felix Geisendörfer** 23:52 Oh, that's a new one. I haven't seen that one.
**Ivo Anjo** 23:56 And you can pick, if you click on the right… on the right thing, you can, like, show also, like, the thing that's been dismissed and updated, so… I don't know, just thought I would mention it since we're complaining about Giza.
**Scott Gerring** 24:09 And it's nice, we don't even… there's not even an outage at the moment, so we can use it in everything.
**Felix Geisendörfer** 24:14 Nick, don't jinx it.
**Scott Gerring** 24:16 Obviously, I have nothing else to say. Thank you for all your feedback.
**Felix Geisendörfer** 24:20 But this is great, Ivo. This is already worth meeting today for me to find this out. If this actually makes it possible to find some previous conversations, that'd be amazing.
But I'm not sure, this says one of 26 comments, where are the other 26?
**Ivo Anjo** 24:34 You need to push the water button, the other button I was saying, the filter one, and then you can say, like, I'll… yes.
**Felix Geisendörfer** 24:42 Okay, so they… okay, okay, so they still want to hide the previous stuff from you, but you can get back to it. Okay, okay. Yes. Okay, okay, okay, this… This might become a new favorite feature of mine. How long has this been there?
**Ivo Anjo** 24:56 I have no idea, someone pointed this to me, like, 2 days ago or something.
**Felix Geisendörfer** 25:02 Wow.
**Florian Lehner** 25:03 What could it and push production.
**Scott Gerring** 25:07 This is probably why the site was down this morning.
**Felix Geisendörfer** 25:13 Well, I mean, if they manage to ship a useful feature for humans and not for AIs, I'm celebrating, even if it causes a little outage.
**Florian Lehner** 25:25 Maybe, maybe, maybe, sorry for interrupting you, not directly related to this, OTEP, but, NEMOX, and Nimroit, sorry, from CoreLogix, opened also, PR on the specification OTEP, to directly make use of the thread context protocol.
So the idea is, from the OB side, that they use, the socket that, were just merged, that, Evo and Scott worked on, to, to push information about, instrumentation about this, socket.
So… information like, hey, is, is this SDK using telemetry? In which kind of telemetry? Something like, are they using, metrics? Are they using traces? From the OE point of view, they want to avoid duplicate information, so, when OE Yeah, 5116, thank you, Scott, for looking it up.
Yeah, I think it's really interesting and shows that, this work is not only For us, as profiling, but also others benefit quite well from it, so that's really nice to see.
**Felix Geisendörfer** 26:51 Yeah, that is really good indeed. Thanks for pointing this out, Florian. Since we have a little time, Scott.
with the reviews, I guess, like, you want a general review, but maybe you could also point people for a second to perhaps controversial bits, or those things that you're the most unsure about in the proposal for people to maybe focus on?
**Scott Gerring** 27:14 That's a, that's something I should be able to answer quickly off the cuff, isn't it? I'm not sure, we've spent so long staring at it at this point.
it… feels like reasonably well-trodden ground to me, but maybe… I don't know, Evo, is there something that jumps out to you that we know has been controversial in the past that you remember?
**Ivo Anjo** 27:38 there is kind of… maybe… there's one thing that I still wanted to look into, is that someone gave me some good feedback that, like, if you want… Our way of, like, we publish the keys separately via the configuration, which is really nice in terms of, like, reducing the size, which is, like, we kind of, like, the size of the context is very limited, so we want to be as… frugal as possible. But someone pointed out that, like, if we're exposing this to users, users might want, like, a bit more freedom in terms of, like, setting their own keys.
And I had this on my, like, to-do list of, like, should we maybe have, like, some option where, like, by default, you can kind of publish the keys elsewhere, but there is some other, like.
you can have a variant where you can publish the keys, and not just the values in mind. If you want to have, like, say, like, okay, this… right now, I just want to have this key. I don't want to declare it, I just want to use this one key, because we're… it's kind of a nice API for customers to use, that they might sometimes just say, like, on this one bit, I would just want to attach this part of information in the code. I don't want to go elsewhere in the configuration and establish a key. So that's one thing that I've been thinking of.
**Scott Gerring** 28:54 So, like, it's a separate… a separate part where we have the… the, the separately keyed section from process context, and then a block below that where you can optionally include both the key ID, or the key name, and the key value inline.
**Ivo Anjo** 29:10 Oh, either that, or maybe we say, like, oh, yeah, if the, we kind of reserve… we could kind of do something, like, we reserve one of the IDs to say, like, oh, if the ID is 255 or something, then, like, the next thing is, like, a key and a value kind of thing. So we could experiment a bit, but… In general, it's more like, do we feel like we need that flexibility or not? I think that's the conversation I… less about the representation, because I think there's, like… as you said, like, we can do it exactly as you say… as you said.
And it would be… work fine. I think the question is more like, do we want more flexibility here, or are we kind of happy with the current amount of flexibility that we have?
**Felix Geisendörfer** 29:51 Is… let me just make sure my notes make… match what you said. Is this about custom labels, essentially, that people might want to set?
**Ivo Anjo** 30:00 Yes.
**Felix Geisendörfer** 30:01 Okay.
**Scott Gerring** 30:02 I think it would be really interesting to know what the folks from Elastic and Polar think about it, because you guys have done this before, basically.
**Felix Geisendörfer** 30:12 Yeah, I think the PolarSignal folks, in particular in previous meetings, had feedback on custom labels, since they built their own solution to that, so maybe you can also, Scott and Ivo, directly solicit them via GitHub, or maybe Slack works better to ping them there.
**Frederic Branczyk** 30:30 Sorry, what was the… what was the specific thing you were wondering about?
**Felix Geisendörfer** 30:34 Oh, Frederick is here. Awesome. Yeah.
**Ivo Anjo** 30:38 The question is more, like, right now we have this… the current implementation, you kind of need to declare the keys ahead of time, and the question is, should we also allow you to kind of just say, like, oh, for this small scope, I want to have, like, a key here, without declaring it ahead of time, because right now, you kind of need to, ahead of time, know all of the keys that you're going to use, or at least update the configuration. And maybe, when we're doing APIs to expose this to customers, customers might want to say, I want, like, a custom key here.
**Felix Geisendörfer** 31:12 Can you say what ahead of time means? Is this stored in the.
**Frederic Branczyk** 31:15 I think I was just gonna say, how ahead of time is ahead of time?
**Scott Gerring** 31:21 Yes, this is also a good point, because the process context is inherently mutable, right? So you always have, with the current mechanism, the option to go back and republish that, but…
**Felix Geisendörfer** 31:33 Okay, so basically, to answer my question, one part of the answer is the keys are currently defined in process context, right?
Okay, and you can update process context if you want to add a new key.
Which seems okay unless you have, like, super high cardinality keys, right?
Which, I don't think you would want that for custom labels.
**Frederic Branczyk** 31:58 It's funny, we actually, we actually just had an incident, surrounding this. Like, I don't know if you saw the PR that I posted last week on Slack, where Go labels essentially produced gibberish, which caused, like, a cardinality explosion in label names for us.
Fun fact. So, yes, we do need to worry about this, but I, I think it's, this, this kind of, ahead-of-time declaration, I think, is… Acceptable from the… from the standpoint of, you know.
We… we should be able to know all the label names.
At process start that could possibly, occur.
I think this is reasonable. We haven't seen anything contrary to that. You know, I… obviously, if you ask someone… enough people, someone will say that they want to dynamically generate label names. I do think that's a bad idea.
But, I worry about this a little bit more from, like, an… library standpoint, like, how… How do we… how do we do this without potentially updating process context all the time?
**Felix Geisendörfer** 33:28 Yeah, Florian, go ahead.
**Florian Lehner** 33:31 maybe not a direct answer to Frederick, but, from a profiling SIC perspective.
How do we want to represent this in the protocol? So, do we just want to take the key that we take from this, process context thread?
and put it as an attribute somewhere in the protocol, and is this what is expected from the customer, or what is the expected action on the custom labels?
**Frederic Branczyk** 34:03 I would expect it to behave exactly the way that Go labels behave today, which is that they become attributes, no?
**Florian Lehner** 34:11 Yeah, but for goal labels, there are explicit attributes in the semconf, and if someone says, hi, I want to have my deck is nice as a key. There is no such attribute in the SEM count for this.
**Frederic Branczyk** 34:31 Okay, then I… In our protocol, it's whatever, whatever labels are transported, basically. And we have a flat label set across, like, we don't have a distinction between, like, resource attributes, etc. It's all flat, and they just get added to that list of labels.
And… We definitely see customers wanting to declare their own like, custom label name. Like, a kind of random thing that we found extremely useful is, in our database, we added the, like, the, like, query plan node name, right? Like, we're never gonna, like, specify that label name as… in, like, semantic conventions, right? So, yeah, I think custom labels is really only useful if Customers can… Specify their own label names, or attribute names, whatever we want to call it.
**Felix Geisendörfer** 35:37 Evo?
**Ivo Anjo** 35:40 I have a question related to this, because I think, to me, this problem is similar to custom attributes in span, so… I know that in Datadog, we kind of, like, throw them all in the same bucket. The Datadog attributes and the custom attributes all just kind of flat, a bit like what Frederick was saying. Does, in OTEL, like, is it the practice that we separate the semantic convention attributes and the custom attributes? I think, like.
Because it seems to me exactly the same problem. If we separate them in hotel in spans, I think it makes sense to follow it here. If we don't, then maybe not?
Kind of thing?
**Florian Lehner** 36:14 Yeah, I think it really depends on how someone configures their collector. There are processors that drop all attributes that are not conformed with OTel, OTEL semconf.
And, yeah, so it comes down to what… someone does in the end. I have no strong feelings. I would just say, hey, these custom attributes or custom labels are not a resource, but just descriptive, so they should not be on the resource level, but on the sample level.
that's the only thing I can think of at the moment.
Personally, I would not enforce Such a cleanup on the collector side.
But that's just, personal.
**Felix Geisendörfer** 37:04 Yeah, I think we… correct me if I'm wrong, but we don't have to worry about such cleanup of non-Semconf labels or attributes for profiling, at least on the sample level, right? Because the processors wouldn't know how to…
**Florian Lehner** 37:17 Yes, correct.
**Felix Geisendörfer** 37:19 Yeah, okay. So unless somebody goes and creates a… profile, attribute sample… sample attribute dropping, processor, then… yeah. So let's… let's just tell people not to do that, or at least not to use it if somebody does it.
**Christos Kalkanis** 37:46 I have a question here for Ivo, maybe Scott as well. So if we allow dynamic keys based on republishing process context, doesn't that introduce races? Because it's an asynchronous operation, right? So the process context is published, but there's no guarantee that the consumer We'll already intide to process the traces with the dynamic keys in order to know what the key is.
**Scott Gerring** 38:13 I think if you ended up in a situation where you had high churn in dynamic keys.
And we wanted to support that. Doing it with constant process, context republishing is for that reason, and probably some other ones as well, maybe not the best way to address it, but… Yeah, Eva, what do you think?
**Ivo Anjo** 38:35 Yeah, I can… I think that would be a problem. I think the assumption… kind of unstated assumption, in a way, is that, like, right now you can add more keys.
Up to the limits, and then after that, you've used up all of your keys. If you start changing keys, then you have, like, exactly this problem, like, okay, like.
this key used to be foo, now is bar, like, I'm reading this context, like.
Yeah. Is this… is it foo? Is it bar? Like, if I… if it was still foo, and this is, like, an old context that the app hasn't updated, what does that mean? I think that's a good point.
**Scott Gerring** 39:15 So maybe the question then for us as a group is, do we want to support Or do we think we need to support dynamic keys at all? Because if we do, then probably we want a mechanism, like Ivo spoke about earlier on.
Or do we just not?
**Felix Geisendörfer** 39:32 My personal take is we don't really want dynamic keys. I think it might be nice to support them in the sense that, like, the application doesn't have to immediately declare them at startup, but, like, as soon… if it can be assumed that the key pass that would retro, so the keys are getting hit early on in the lifetime of the service, and then stay relatively, yeah, the same without new additions. I think what we have is fine. I think we want to actually discourage people adding keys on a frequent basis. I think if they have a use case for that, I think they should use one key and just put a more complex value into the key. It's my take. Here is what other people think.
**Christos Kalkanis** 40:11 Yeah, I would agree with that. And if we don't strictly need it, I don't see no reason to even allow the possibility of such complexity. Sometimes if you leave a mechanism open.
it's going to be used, and then you have to deal with the repercussions of that. So it's actually easier to, you know, ensure from the beginning that this problem cannot exist.
**Florian Lehner** 40:38 Also…
**Frederic Branczyk** 40:38 How exactly are we suggesting that we prevent this from happening? Because if process context can be… Refreshed when new… Label keys have been used, for example.
then… How is that really all that different? People can still add arbitrary things.
**Felix Geisendörfer** 41:04 Sorry, Ivutu, go ahead, but I think the simple answer is, like, there's a limit of 256 keys right now, if I saw this correctly, so at some point you're going to get an error if you're trying to register another key.
But until you get that error, you will basically… what we would do in the background, I assume, is to update process context. Every time you add a key, process context gets republished. Up until it hits a limit, then you're being told, like, you are using this the wrong way, you're holding it wrong. Resync what you're doing.
**Frederic Branczyk** 41:30 Okay. I still worry about the, like.
developer experience of this, but, like, in general, I don't… I don't feel too strongly. I will say, like.
just putting the, like, label name and value into, like, into every sample hasn't really been a problem for us. That's how our custom labels approach has worked.
But, yeah I don't think I feel too strongly, as long as we can get the developer experience right.
And, libraries.
Sorry, I go.
**Ivo Anjo** 42:12 So, yeah, I have a few notes about this. Like, one is that I think this call-out about, like, the keys, make sure to document in the spec, kind of say, like, okay, you're not supposed to… you're not supposed to swap existing keys, you're supposed to keep adding keys, and once you run out of them, you run out of them. I think we can kind of do that. And as a kind of a follow-up of that note.
Technically… I… I think this is something that it sounds like we could evolve. So it's… I wouldn't say it's, like, a pure two-way door kind of thing, but it, like… doing it today or doing it tomorrow, like, it feels like this could be a kind of, like, evolution. It's like, say, oh yeah, we have, like, an old, like, writer that doesn't support dynamic keys, and then writers can now have dynamic keys and whatever, so it feels like something that we can kind of evolve if we have the need.
There is one… I think, to me, the biggest advantage of doing this right now is that, you… it allows you to have a very simple thread context implementation that is, like, kind of fully decoupled from the process context.
Because you can kind of say… once the process context, you could kind of say, oh yeah, the process context, there is a thread context.
And then the thread context can, like, change keys, red keys, whatever, and never needs to update the process context again. You can have… you can even implement the thread context without process context, which… Not sure if… whatever, but I'll kind of say… you could kind of say, like, I don't even care about process context, you can fully implement red context, and you have your own keys and whatever, and that seems like something that would be nice, but again, like, is nice enough of a bar here for us to actually support this, or no?
**Frederic Branczyk** 44:01 I don't think I can completely follow. How can threat context be useful without process context, if process context is how we declare label names?
**Ivo Anjo** 44:13 Because if you had, like, the fully dynamic keys, you could say, like, oh, I never use the ahead-of-time declared keys, I always use dynamic keys, and so I don't even need to know about process context.
**Felix Geisendörfer** 44:24 You're basically hinting at a, like, extended version of thread context that we don't have yet, where you could have dynamic keys, right? Is that what you're saying, Evo?
**Ivo Anjo** 44:33 Yes, yes, exactly. I'm saying, like, this would be one advantage of having dynamic keys, is that you could kind of implement, like, one thread context that is completely independent from process context.
Which would be more inefficient, for the reader, and you'd kind of be wasting a lot of time in your… a lot of space in your keys, because the eBPF Profiler has, like, a limited, so you'd spend… your very valuable bytes of, how much context we can get in the eBPF profiler would be spent on, like, keys.
I know.
**Frederic Branczyk** 45:03 Right, that's exactly the part that I mentioned earlier, hasn't really been a problem for us.
So, like, if we… I guess, like, I'm happy with us starting with declaring the keys in process context, and then if we figure out, oh, this was, you know, a bad idea, or for whatever reason, it's still very useful to not have process context and only thread context.
then we can extend it, yeah. I think I'm happy with that path.
Though I'm not sure we'll ever get there.
**Scott Gerring** 45:37 I think that sounds all very reasonable. If… if you all like, I can all… I can ping everyone who's had an opinion about this on, like, that block of the OTEP as well, and just say, hey.
Let us know what you think, and then we can roll it out that way, and kind of get an agreement, just to make sure we're all on the same page.
**Felix Geisendörfer** 45:55 Yeah, I think that's a good idea, and everybody who was just thinking about this, like, yeah, make sure to review the pull request and give your Feedback on it.
**Scott Gerring** 46:04 And thanks all for the discussion. It seems like we've totally dominated this meeting, but it's good that people are interested in this stuff, I think.
**Felix Geisendörfer** 46:11 This meeting needed something to be dominated by. We had time. Speaking of, I do see Alexei has joined, so we should probably return to our… Skipped items, unless there's anything people want to add here.
Going once… Going twice… Okay, I'm gonna take us back to the, previous… a review of action items. I think let's start with this one, because that's the one we actually covered first.
So, Alexei, I think Christos mentioned that you might have feedback on the proposals that Florian and I cooked up for dealing with the fact that we have a unit right now in the protocol, and so we had, just a reminder, we had one proposal from, Florian to actually make Unit a first-class citizen in, key value as, like, a new field. And with a proposal from me to do something more hacky with, semantic conventions and attributes to handle units, and we are curious if, yeah, if you have thoughts.
**Alexey A** 47:26 Sorry, I didn't have time to… take a look. I should… I think when with the first proposal, for, like, using semantic conventions.
I think there's a proposal to, like, encode the unit in the tag name. Do I recall this correctly?
**Felix Geisendörfer** 47:51 Yeah, I can… I can… I can quickly open it up again, So the… the rough idea is that… you would basically, have a attribute called p-proof num units.
And this attribute would basically be a complex attribute, which is a map with multiple keys and values, and the keys would be all the attributes that are used by the payload that actually have units associated with them. So here's the name of the attribute, and here's the unit.
That's roughly the proposal. There's already some good feedback from Christos, which is still under discussion there, so maybe some details will change, but the high-level idea is, hey, instead of making the unit part of the protocol, let's just have an extra field Or, sorry, an attribute, where we can define which attributes have units and what the units for those attributes are. That's… that's a key idea.
**Alexey A** 48:47 one… one question I think I would have is, like, is this really… And we would do this, okay, we would do this with… so we would basically use, like, different conventions for PProf and for… non-P-proof profiles, because for non-Proof profiles, we would use, semantic conventions.
We also have the unit for the actual sample type.
So, is that there is also inconsistency in how we treat labels and sample types? Because for sample type, we do include the unit explicitly. And also, one argument, I think, was that include… one problem with including unit is, like, how we declare what the unit should be, because OpenTelemetry uses this convention. Sorry, I forgot the acronym, but there's this specific standard for how to express the units.
**Felix Geisendörfer** 49:38 Yep.
**Alexey A** 49:39 And then if we do that, but people of, like, the legacy people of things cannot follow that standard, and then we… kind of like, what is the guideline we should give for that? But that also applies to, like, what do we do about sample type units, then? Because we also have sample type units, and Piprof will have the same problem there, so I think this is where my… And I, I, I haven't, like, I haven't… I haven't fully took this… This train of thought.
trip, but this is what I was thinking of. Like, labels versus sample types. We have units in different places, and, like, do we want to treat them consistently?
**Felix Geisendörfer** 50:20 Yeah, I think, I think there's, Definitely many things to consider here. I think one of them is just, like, the fact that we added unit to a common protocol element in OpenTelemetry has, like, caused upstream issues, so I think it's currently considered a blocker for us to ever go to beta, so that's why we have to care about it.
with high priority, making it nice and consistent with what we have for units for sample types would obviously be great, but I think it's slightly a P2 in comparison, because that's More of an aesthetic thing to some degree, than it is, a blocker for the better, I would say. Maybe aesthetic is putting it too lightly, but nobody's gonna challenge us on that outside of our own sake, I would say.
But I think, Alexi, if you could take some time to take a look and leave some comments on the document, or on both documents from Florian and myself, that'd be really appreciated, because, yeah, that's.
**Alexey A** 51:16 And what are the… I assume, like, the upstream issues you mentioned are summarized in the document?
**Felix Geisendörfer** 51:22 I forget where we have the upstream issue. Oh, wait, it's on the… so we have the better roadmap here.
I think the key unit thing has… Where is the unit thing? It's one of C's, I forget which one. Oh, okay, it's called… Profiles reinvents the attributes. I think this is essentially the one…
**Alexey A** 51:45 Okay, it's that one by Bogdan.
**Felix Geisendörfer** 51:47 Yeah, by Bogdan, exactly. This is… this is the original thing, and the last comment here is basically the proposals.
I can, I can link that in the Sikh meeting notes.
**Alexey A** 52:01 Okay, and does Tigrant have an opinion? Because my memory is that in the past, there was… like, we never had anything concrete, but there was… general and broad feedback that, well, maybe units are useful for OpenTelemetry as a whole.
as well.
**Felix Geisendörfer** 52:22 I would say that… Bogdan is likely to have opinions if we propose something to the main protocol. The challenge is going to be how fast we can get those opinions from him, and… That's sort of maybe one of the aspects of proposing something more hacky, but I… I think the idea is to sort of push both of these ideas forward and, like, get feedback from the TC on their appetite. Like, if the TC says we have appetite for tackling unit in the main protocol, then I think we should probably proceed in the direction of Florian's proposal.
If the TC is like, we're totally swamped, it's gonna take us a year for us to consider talking about units.
then maybe we would have to do something with semantic conventions, because as useful as units are to some degree, they're mostly in the protocol right now because of PProf, I would say.
**Alexey A** 53:11 Okay.
**Felix Geisendörfer** 53:13 But I'm happy to be challenged on this, honestly, so I don't feel too strongly.
But, yeah.
**Alexey A** 53:19 So, like, the ultimate goal for beta is get rid of this profiling-specific key value and unit type, and, like, and figure this out one way or another.
**Felix Geisendörfer** 53:30 I think that's a good summary, I'll capture that here.
**Alexey A** 53:42 Maybe this is the, like, kind of like… Paperwork trail-wise, maybe this is the… the issue we… I think this is, like, effectively what Bogdan's issue is, but it's not, like, spelled as explicitly, I guess.
**Felix Geisendörfer** 53:58 Yes.
**Alexey A** 54:01 Okay. Yeah. I'll take a look.
**Felix Geisendörfer** 54:04 Cool. And maybe the next step here, honestly, is to get the TC to look at Florian's proposal, because I think it's also pretty good. I think the only concern that we had there is that it's going to take a long time to get any traction on it.
**Alexey A** 54:16 Yeah, I think getting some, like, temperature check with TC would be good. Is it, like, yeah, like, we're enthusiastic to figure this out, because we, like, had 5 conversations recently about how units would be useful.
Versus, well, if you figure this out for us, then we are happy to take best effort to review this, or versus, like, no, we actually don't want this. If you get rid of this, we'll just be happier.
Like, on a scale from 0 to 100 would… Where are they?
**Felix Geisendörfer** 54:49 Yeah. How about this? I think it would still make sense for you to, like, if you get a chance to look at it, but I can update my action item here to ping the TC next.
Where am I?
Mmm…
**Alexey A** 55:05 Let me tag myself so that it doesn't escape my…
**Felix Geisendörfer** 55:33 Okay, yeah, I can text this to ping the TC, I'll probably… started spread in Slack, Okay, I think we should move on from this item, because we have only, 5 minutes left. In terms of using them, if somebody has something urgent before we, head to the end of the meeting, please interrupt right now. If not, I would go through the remaining to-dos from Alexei, and then… go to my review better roadmap even, so I don't think we'll get to it.
Okay, I see you're updating stuff here, maybe…
**Alexey A** 56:18 Yeah, I think it was in the wrong place, because this PR was for, for clarifying period type and… period semantics, there also, I think… was it copy-pasted from above? I wonder if I miscaptured it there. Oh, no. No, I think it's, Difficult.
**Felix Geisendörfer** 56:39 If you haven't done any major changes to these, then you can also just update the to-dos later in the.
**Alexey A** 56:45 Yeah, like, there was no, there was no significant, like, there's, there's no major update, we can, we can move on.
**Felix Geisendörfer** 56:51 Okay.
Cool, then I'll leave it to you to, like… I think the most useful is to update the top section, because that's what we're going to copy in, and if we forget the last meeting, then it's nice to have some reminder there.
Okay, then I want to briefly, entertain the better roadmap.
And just quickly review it with everybody, basically, I created a meta issue again, similar to the one that we had for the alpha, to try to capture all the things we should do before we could call this protocol better.
it is possible that I forgot stuff here, and that we'll discover new things, but I think, to the extent possible, it's kind of nice to have an ongoing meta-issue.
So yeah, basically the payload sizes was one issue here. The key unit one is another big one. Handling original payload from Jonathan that we discussed earlier is one. Finishing the documentation work is definitely needed.
Better docking samples for period type and period fields. I think that makes sense to sort out.
This is, I guess, related. Is that the same one? I think they're separate, but I forgot the details.
Yeah, here's another one about sample types, not to be confused with period types.
And… We also need to look at our interactions with OTTL, because we're using UN64, and I think OTTL only supports UN64, so when we get to very large UNs, it's gonna get interesting.
with OTTL, And yeah, this is basically the rough list. Does anybody see something major that, let's say, would like to add here?
Or has any thoughts on… Some of these things not belonging on the critical path, please let me know.
If not, then, yeah, just a reminder that we have this issue now. If you ever want to check, like, what's still pending, and you're looking for something maybe to help with, I think going down this list can always be useful as well.
Sweet! I think that gets us right to the end of the… end of time.
So, unless anybody has any lost thoughts… I would say thank you all for joining, thank you all for your contributions, and have a nice local time.
**Ivo Anjo** 59:34 They're on…
**Frederic Branczyk** 59:35 See ya.
**Felix Geisendörfer** 59:36 Bye.
