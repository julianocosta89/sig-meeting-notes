SIG: Specification SIG
Date: 2025-08-19
Duration: 46 minutes
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 00:29 Hello.
**Liudmila Molkova** 00:32 Hello, hi, everyone. Welcome to the specification meeting.
And I am going to drive it today, since we are now rotating on who drives the call.
Give me a second to prepare, and… We will get started.
Okay, so we… while we're waiting, please add your name to the attendees list. If you have something to discuss, please add it to the agenda.
K… R… So, I'll give people a few more minutes to join.
Okay.
**Kayla Reopelle** 02:09 Hey Lyudmila, could you share the meeting notes link? I'm… I'm getting, like, a file does not exist when I click on the link in the calendar invite.
**Liudmila Molkova** 02:19 Sure, so here you go.
Can you access them now?
**Kayla Reopelle** 02:27 Yep, that worked, thank you.
**Liudmila Molkova** 02:29 Nice, thank you.
**Tristan Sloughter** 02:33 There's a difference between the note link in the body of the meeting.
**Liudmila Molkova** 02:40 like, the….
**Tristan Sloughter** 02:42 Message about the meeting, and then there's the… attached Google Docs, and that's the one that doesn't work. I don't know if that could be updated or something.
**Kayla Reopelle** 02:50 Got it.
**Liudmila Molkova** 02:51 Oh, that's good to know.
Okay, I'll check.
Right.
Let me see if I can update the calendar.
But I think we have, people now… 10 participants… let's… Get started.
I think Robert is not here.
So let's take a look. The… there's a pull request.
That removes… are the… Note on extending… A set of standard attributes being a breaking change.
So the RTEP is merged, and now this POR removes the node.
that disallowed complex attributes. There are a bunch of approvals.
And it's been out there for… Quite a bit.
There was no discussion, so I'm actually… Going to merge it after the call.
If you have any last-minute comments, please comment, otherwise it will be in by the end of the day.
… Let's move on. Gregor.
Do you want to present? Do you want me to present?
McGregor, are you here?
**Carlos Alberto Cortez** 04:42 He's not.
**Liudmila Molkova** 04:44 Okay, I think I saw him.
So maybe there was some problem, let's move it down.
Let's see if he is back.
it to Rusk.
**Trask Stalnaker** 05:04 Yeah, so just wanted to bring to this group, the YAML-ification of, the spec compliance matrix.
So this first PR is, just trying to, maintain status quo, to verify that, you know, all the check marks Came back in the right place.
So, like, if you go to the… markdown file, and you look at it with white space, ignoring white space.
You should… so try, … Ignore white space up under the gear icon.
Top middle.
Top of your screen, there's a gear icon.
**Liudmila Molkova** 06:03 Oh, thank you.
**Trask Stalnaker** 06:05 Yeah, a hide white space, yeah.
**Liudmila Molkova** 06:18 Nice.
**Trask Stalnaker** 06:19 Yeah, now, there was, one… so we do, part of this is following recommendation from the, the TC in, issue previously about splitting YAML… splitting these out into language-specific YAML files, which then could eventually live in the, language repos.
One thing, once they live… once we move it into language repos, it's going to be, like, right now, the feature mat… the matching is done just based on this name.
And so if somebody wanted to update the name of one of these, for example, we would have to go and update all those different repos.
Which could be annoying. So I don't know if folks had any… had thought about that already. That can certainly… I mean, I probably wouldn't do that in this PR, but kind of… as the… I want to work out all the YAML details in this repo before we start splitting them out into other repos, since it'll be painful to update after that.
I mean, to do, like, global updates. It'll be easy to do language-specific updates after that, which will be nice.
I mean, the most basic thought was I can throw, like, a key that's just generated either a feature 1, Feature 2, or just based on, you know, underscoring these existing names that then wouldn't change over time from the displays.
….
**Liudmila Molkova** 08:16 If anybody has….
**Trask Stalnaker** 08:17 Yeah.
**Liudmila Molkova** 08:19 We would still be able to validate this, right? So, there could be a validation that checks that all of the features are recognized.
And none of the… features are… New and not available in the central place.
**Trask Stalnaker** 08:38 Yeah, yeah.
So maybe this is fine.
It's certainly simpler.
Not to throw random keys in there everywhere.
So, mostly just wanted to bring attention, … Also, if you look at the… if you have any suggestions for the YAML structure, please feel free to leave them on the… on this PR, or on the issue that it links back to.
And I'll take that into consideration on the next, changes.
**Carlos Alberto Cortez** 09:23 Did you use, Copilot or something for this? I'm guessing yes.
**Trask Stalnaker** 09:29 Heck yeah.
Although, actually, Copilot wasn't very… Copilot, it worked. It took several tries. Eventually, the best thing was to tell Copilot to generate a script.
to create the YAML files from?
**Carlos Alberto Cortez** 09:53 Nice.
**Liudmila Molkova** 09:57 This is wonderful. Thanks a lot, Trask, for doing this.
**Trask Stalnaker** 10:03 Yeah.
Yeah, thanks.
It was, Kayla's, latest PR and questions about, how to deal with experimental and non-experimental attributes that, motivated me, because that's… that would also be a good follow-up here, is now that we have, YAML declarations to… and that's in that issue. I think that was actually what started the issue, was, How to mark things that are experimental versus stable in repos.
So I think there's some good follow-ups here.
**Liudmila Molkova** 10:43 So we would have an extra status for experimental things, or something around that.
**Trask Stalnaker** 10:48 Yeah. Yeah.
**Liudmila Molkova** 10:51 Okay.
Cool!
That's awesome, thanks a lot for working on this. This is very exciting. And you are still on track with pull request 700.
**Trask Stalnaker** 11:07 Yeah, I just threw this on since Tigrin's here, I thought we could have a… just a… quick real-time, discussion. The, so for this, Tigrin, are you okay with making the profiling… profiling, maintainers maintainers? Can we make them maintainers of this repo?
Just because we don't have… oh, go ahead, yeah.
**Tigran Najaryan** 11:36 Maybe it'll help if I maybe explain what the context is, right? So, with this repository, the product repository, it contains all of the signals that we have at OpenTlem, actually. And then, we have, essentially, a profiling sync, which is responsible just for the profiling signal.
And, they, they needed, essentially, an ability to iterate quickly on the profiling proto.
As they were working on the, on the, essentially, initial format for the profiles in OTLP.
And the… the arrangement we came up with is that essentially, the maintainers of the profiling SIG, So they are… we know them as maintainers of the profiling seat. They, needed a way to… to be, essentially, approvers on this repository, so that, essentially, their approvals count against the official requirements, so that we can merge the PRs there.
Now, we also have approvers of the profiling seat.
I… so, here's the thing. This PR merely captures that arrangement, that we have profiling maintainers, we have profiling approvers. It doesn't change anything in the actual permissions that these folks have.
And I don't know, to be honest, if we're using the GitHub's permissions capabilities the right way here.
The question you're asking, I'm not sure what the right answer to that is. This merely lists the maintainers and approvers of the profiling SIG in the README file, just like we do for, I think, most or all of our other repositories.
And … the permissions part, I think it's open for discussion. What is the best way to reflect that reality, that we have people who need to be able to At the very least, approve changes on a subdirectory of this repository.
But I'm also fine if that approval is essentially, a bit, I guess, wider, but permission is a bit wider than they actually need. I think we… we trust these people, so I don't see a problem, per se. If we… if there is no way to reflect this granularity using GitHub's capabilities.
in that specific narrow way I was describing, I think it's okay to have that a bit, I guess, wider permission so that they… the approvals Are technically possible against all of the changes that happen in the repository.
I don't think anybody's going to, I don't know, do anything malicious here.
**Trask Stalnaker** 14:29 Everything that… everything that you've described about what the profiling maintainers are… want to be able to do in this repo is… Covered by… and the existing state in this repo is that they are approvers.
They are not… they are not maintainers in this repo today, if you're trying to reflect current state.
They have approval rights, they are in the code owners as approvers.
So everything they're doing today is what, … Pro is what a repo approver in code owners does.
If the difference with Maintainer is then they get the right… if you… if they want the ability to hit the merge button.
And they want the ability to make releases.
then they're a maintainer, and I think that My recommendation would be not make… we don't really have that concept of a… Component maintainer, anywhere, in any other repos.
So my recommendation would be just make them a global, a maintainer.
And then they would… that is a maintainer. They can hit the merge button, and they can make releases.
**Tigran Najaryan** 15:46 I think that's fine, we can do that. I don't mind that.
**Trask Stalnaker** 15:50 Okay.
I will send a, PR to the admin repo to make them maintainers.
And in this repo, I would just suggest remove the signal-specific Peace from the maintainers, because… We don't have that concept anywhere else. They are just.
**Tigran Najaryan** 16:11 You mean in the README as well? Remove that in the README.
**Trask Stalnaker** 16:14 In the README, yeah, yeah.
**Tigran Najaryan** 16:16 Okay.
Yeah, I can do that. It's fine. It makes my life a bit easier, because I had to hit the merch button myself as the sixth sponsor in the past.
**Trask Stalnaker** 16:24 Yeah, yeah, yeah, I mean, that's fine, that is, yeah, totally fine.
**Tigran Najaryan** 16:29 Okay, cool.
Thank you.
**Liudmila Molkova** 16:33 O'Reilly has his hand raised. You wanna go ahead?
**Reiley** 16:36 Yeah, so Charles, I agree with what you said. Do you think it's the right time for us to create the protocol maintainers and approvers group instead of reusing, like, the TC spec sponsor? Ideally, I want to separate them.
**Trask Stalnaker** 16:53 I'm… it's fine. I'm totally 100%.
**Tigran Najaryan** 16:57 Yeah.
**Trask Stalnaker** 16:57 100% fine either way.
**Tigran Najaryan** 16:58 That's a good proposal. We can actually… essentially, we could make these people who are profiling maintainers, we could also put them in the group of the proto-maintainers, essentially, right? So that it respects the permissions they have on this repository.
**Reiley** 17:15 I'll Facebook groups now.
I'll create the groups and add the right people there, and we can start by having the… the profiling folks, like, from your list, Tigran, as, added as maintainers, if you agree.
**Tigran Najaryan** 17:30 Yeah, yeah. And we need them in the README, just to be clear. The reason I needed them in the README is that we wanted to move, we wanted to add an approver And there is no way to reflect it anywhere in the repository. That would only be, I guess, visible in the audit logs if you go look at the permission changes, but I think we need that visibility in the read refuge, like we do in every other repository.
**Reiley** 17:55 Would you get their explicit acknowledgement that they want to be the maintainer?
Yeah, yeah, yeah. Sign up to be the maintainers. Okay, thanks.
**Tigran Najaryan** 18:03 having this tracking tracked in the commit history, I think, is a nice way of… Of doing this all day block.
**Reiley** 18:11 Okay.
Thanks, Ron.
**Liudmila Molkova** 18:18 Cool.
Thanks a lot, great discussion. Kayla, do you want to go ahead with this issue?
**Kayla Reopelle** 18:26 Sure, yeah. Do you… I… could you open up the issue that's linked?
**Liudmila Molkova** 18:34 Oh, I'm sorry, I'm not sharing, right? I'm sharing wrongly, no. This one.
**Kayla Reopelle** 18:40 Oh.
Yes, that's the one. Yes. Wonderful.
Recently, like, we've been working on, getting metrics ready for Ruby, and one of our users reached out, to ask about not only the status of this issue, but also about the possibility of exposing some sort of instrument registry so that people could access instruments after they've created them without necessarily, like.
Saving a hook to them.
And so, kind of using… I guess there's two questions. Like, first is, you know, this issue hasn't been worked on for a while. I was kind of wondering if there was any context about it that wasn't represented in the comments, or if people had thoughts about Kind of bringing it… backup for discussion. And then the other element is, I guess, like, what's the background on… not providing, like, an API to access instruments after they're created, and, you know, would that be something that could fit into the spec?
So maybe starting with, like, unregistering things, … Are you aware of any, like.
Blockers about this one that are particular hairy.
particularly hairy, so that's why we're not working on it. … Or is it just something that kind of got lost?
**Carlos Alberto Cortez** 20:05 So, I think it got kind of lost. The main summaries are two comments that are next to each other. The first one is from David Ashbold about the current state of mothers and potential workarounds.
The second one is from J. McD, providing some more details. A little bit more down, please.
Yes, that's one, that's the first one, and the second one. So, the first one is David Ashburn and Jay McD.
about what remains to be done to fully do this, because there are, as I mentioned before, some potential workarounds around this. After that, I think there was no interest from many people.
So, there were other priorities. Jim ID is in the call, so he may know more about, whether something was done after that, but I think nothing was done after.
**jmacdonald** 20:55 Yeah, I don't have a ton of, context that's new. I remember the issue.
there… there always was an effort in OpenTelemetry to keep the API, sort of, whatever's necessary for the instrumenter, and this… this always… made it look like a kind of SDK kind of question, like, what instruments are registered. There was some work to get it possible to unregister asynchronous callbacks, since that's something where an instrument really needs to be deactivated.
And then I know there was… I mean, I can just regurgitate what I remember from this thread, but I won't. Like, something about delta versus cumulative making it slightly tricky, and the conventions of Prometheus. I'm not ready to talk about this one, though. I would like to see what Tristan has to say.
**Tristan Sloughter** 21:45 Oh, I was just gonna say that in the… the Erlang implementation, we do have the concept of, kind of, registering instruments, so you can refer to them later by a name, so you can give a name, and then you can refer to it later, and that's because we don't have global variables, so it kind of was just a necessity there, and … and how people were used to working with metric APIs for other implementations, like Prometheus and StatsD.
So we didn't go through any formal process for that, because it seemed like it was just something necessary to us. If there's, others that are interested in something like that, I'd be… more than happy to collaborate on that, and I also have seen some the developer experience SIG. I think some stuff on the developer experience for metrics would be cool if we helped out with, so… If you want to also join in there, and, propose, if you think it fits.
Our mission, then that would be… A nice place to bring it up, I think.
**Kayla Reopelle** 22:48 Okay.
Nice. Yeah, I feel like the… the registry… I'm glad to know it's in Erling. I'll kind of take a look at that implementation. I feel like even though Ruby has global variables, it's really discouraged to use them, and I think it would be a lot cleaner and a lot more aligned with, kind of.
the… the ways that we use other libraries to have some sort of registry, but since I still feel kind of new to, like, specs and also, I guess, implementing things that aren't part of the spec, and what's allowed and not, I thought I'd bring it up here to check before, I guess, just trying to build a prototype to see how that would work.
But yeah, I'll, check out the developer experience SIG. I'm curious to learn more about, too, how other… users, like, use metrics and refer to their instruments, because maybe there's a good pattern that we just haven't thought of yet that other folks are using, so that this API wouldn't be necessary.
**Liudmila Molkova** 24:02 I think there is a pattern, and when you create an observable instrument, that you get a handle of this instrument, and you just carry it around, and then you dispose it of some sorts.
seems to be, like, the cleanest pattern, and what can go wrong with it. So I would be kind of curious to learn why people would not do this, or are they lazy, or … Is… is there a real user experience problem with not… Providing the way for them to get this handled later on.
**Kayla Reopelle** 24:37 Yeah.
Sounds good.
Yeah, I don't… I don't know enough of the answers right now, but I'll….
**jmacdonald** 24:44 As a user who has dealt with StatsD codebases in the past, I know that it's frequently expected that you can just produce a string and turn it into a metric, kind of on the fly, and I think there's been a lot of resistance, or there's just a lot of trouble when you try to do that with an OTL API.
You end up building a map of instruments by name or something like that.
It's sort of a mess. So I've definitely seen, as a user, like, the user experience is not good. And if we can fix that, I would be supportive.
However we decide to do that.
**Tristan Sloughter** 25:20 Yeah, I can say, in the Erlang case, you want to create instruments in one process, like, the instrumentation library.
For a web server, it comes up, and it creates the instruments, and then you want to use them in some other process that is spawned in another… some other module has a function spawned, and you want to use it, and passing it between there is just not… Feasible in many cases, partially because of just how… The instrumentation libraries have to be done, in their… in these web servers, so, like, passing it through isn't an option, but then… it would just still be, like, a map to look up the name in another data structure instead of a global one, so it's really sort of the same. And the ways I've seen it done in other languages, it often seems like it's just global variables, which Certainly can be nicer for some things like this, so you just reference it by name, and so you always know you have that.
That actual instrument, and not just some name that could or could not exist, but yeah, it just wasn't… Wasn't an option that I was feeling was very ergonomic for our users.
**Liudmila Molkova** 26:36 Alrighty. Thanks for the input. Any other comments on this?
Okay, let's move on to the next topic. Gregor, are you here, now?
We try to….
**GZ Gregor Zeitlinger** 26:51 Yes!
**Liudmila Molkova** 26:52 Yeah, wonderful.
**GZ Gregor Zeitlinger** 26:53 My computer was just crashing at the beginning of the meeting.
**Liudmila Molkova** 26:57 Oh, yeah, we were not sure if you were around and if you were coming back. So, do you want to talk about this one?
**GZ Gregor Zeitlinger** 27:05 Right, yeah, so this is a really old issue, but what I'm really working on is declarative configuration for Java.
And this has come up because, we, have the capability to configure exporters, Right now, and we want to retain that capability with dynamic configuration, and right now, we have a GCP, authenticator in our contrib repository, and that works because it can set headers dynamically.
And, … I actually have an issue linked that describes exactly the Java … set up. I think it's at the end of the… Issue, right, yeah.
Probably good to look there, because, … of all the possibilities that we might want to support, this is what I'm… interested in, and maybe we can start with a small setup. If you scroll down, you can see, the setting exactly there.
So this is, the, GCP authenticator SI… propose. It could be done for declarative configuration, but declarative configuration does not have The concept of authenticators so far.
Collectors do, however, and I just put it there as a reference, but I learned that this is not something at the spec level.
And that's why I'm here.
So my question is, … how, … first of all, do you like the idea of the authenticator? And second, question is, … Can we, make this a step-by-step thing so that I can, Add support for, what is… Possible right now, because if you look at the original issue, it talks about a lot of different things.
Authenticator, types. This was in the original issue.
… Yeah, so I'm trying to find out how to slice and dice this.
**Liudmila Molkova** 29:38 By the way, Gregor, have you seen there is a not tap, on this? I'm trying to find the link.
Sorry, I'm going to paste it in the chat in a sec. It's 4 105,000. There has been an attempt from AWS recently to define one.
To define the interface.
And, there were a lot of comments there that he might find useful.
**GZ Gregor Zeitlinger** 30:16 here in the chat, got it.
**Liudmila Molkova** 30:18 Yeah.
So I think Jack had some points on the Java site in the past, and if I recall them correctly, the key challenge to make it truly configurable in Java is that … It depends on the HTTP stack or gRPC stack implementation, and the HTTP client, and it's actually relatively hard to have an abstraction.
over different HTTP clients.
But I see Trust raised his hand, he has more input on this.
**Trask Stalnaker** 30:54 Yeah, so I think that was a little bit more specific to… in the AWS case, they want to… they want to be able to hash the request, the content.
That's sent over the wire.
This modifying headers… is something that's already available in the Java SDK.
And that's what these authenticators that we have today are doing already.
What we don't have is, if I'm… getting this right, Gregor, what we don't have is the concept of a named authenticator that we can then leverage in declarative config.
**GZ Gregor Zeitlinger** 31:41 Yeah, the term is a component in declarative configuration. Basically, it is not a first-class citizen, and also, therefore, it doesn't have a name.
**Carlos Alberto Cortez** 31:55 Because authenticator is not in the spec, correct, at this moment, if I remember correctly.
**Trask Stalnaker** 32:00 Exactly.
**GZ Gregor Zeitlinger** 32:01 Exactly. That is what we also found out in the declarative config meeting, because declarative config tries to build on the concepts defined in the spec. That's how These things are related.
So, a Trask, … Could we, … hash out a very simple… Subset of authenticator that says it has a name, and that everything else is up to implementation, or is that not a viable option?
**Trask Stalnaker** 32:43 I would probably at least include, the header, you know, updating headers, since that's pretty standard for… that's the most common use case for authenticators.
**Carlos Alberto Cortez** 32:56 Yeah, I agree with that, especially that the collector has this for… I mean, as long as you understand that it's very specific for HTTP and GRTP, you know? I think we should be fine.
Overwhelming the limitations that it's only headers.
**GZ Gregor Zeitlinger** 33:12 Is there anything special about gRPC headers?
**Carlos Alberto Cortez** 33:17 No, no, I mean, like, like, there's no funky authentication other than headers. Like, no AWS hashing or anything like that. It's just, like, a specific component that provides headers, and if your transport is happy with custom headers, that's okay. If not, well, we don't support that.
**GZ Gregor Zeitlinger** 33:37 Okay, how would I, proceed, to do that? Write a… pull request that lays out how this should be done, or should I start with a reference implementation? What's the best… Idea.
**Carlos Alberto Cortez** 33:54 I could say an issue, I'm just linking to your prototype, so other people can review that.
**GZ Gregor Zeitlinger** 34:01 Okay, so it needs a prototype. Currently does not have one. Okay.
**Carlos Alberto Cortez** 34:05 Yep.
**GZ Gregor Zeitlinger** 34:06 Okay.
**Trask Stalnaker** 34:08 Yeah, generally for the fir- like, the first PR that proposes something like this would need one prototype, and then… The stabilization later, at some point, needs 3… More baked prototypes.
**GZ Gregor Zeitlinger** 34:26 Okay, cool, yeah, I'll start with that.
**Liudmila Molkova** 34:34 Cool.
Thanks a lot for the great discussion. Josh, do you want to talk about something?
**jmacdonald** 34:45 Yes, just briefly, see if I can sh… oh, you've got it up. Okay, so, ….
**Liudmila Molkova** 34:51 Wanna share?
**jmacdonald** 34:52 Sure, I'll share just a minute. So, one thing here is Kayla and Gregor both put up a very, very old issue, and I have one too.
… So, here it is. … And the… so, if you recall, the OTEL group was finalizing its 1.0 trace ID spec around January of 2021.
At least that's how I would call it. And, so there's this issue that was filed, this number 1413, and I've linked to it here. It placed a to-do in the spec for the trace ID ratio sampler, saying this is not finished.
And I've been working on it for a while, so we've got some OTEPs that are done, and they've merged now, and this is a, a response from a few weeks ago, I believe.
the GoSig was concerned that users were depending on the current features, so now I've rewritten the spec change from the latest OTEP.
And, what I want to tell you what I did. So I've changed… so I've restored some text from the old… before my changes, so before my change number 4166 specifically, which redefined trace ID ratio-based.
And the reason I wanted to redefine it is, like, it had a to-do, it was never specified, so, like, I thought it was kind of broken, but I agree that there are cases where the existing behavior has to be preserved. So, what we're doing then is marking the trace-80 ratio base deprecated. I've marked it as deprecated and not to be removed before January of 2027.
And otherwise, I didn't really change it. This is, like, basically the same text on the screen as it used to be before my PR. And I'll show you what I changed.
So, … So, there… this was… this warning was always there. I changed it just a little bit to say that the, that the… that it's considered unstable. The trace-ady ratio-based Well, implementation is considered unstable. Always was, but that was the… the text is a little clearer ago.
And then as part of the change that I made, we were trying to introduce, like, a deprecation plan so that it wouldn't be so painful on users to just, like, replace this on them. So there's three warnings discussed in this document, and I've refined them based on the feedback I got the last time.
So if you're a trace ID ratio-based sampler, and you're being used after this work here, you have two options for giving a warning to the user to tell them that they're doing something that's, like, deprecated.
So… so this was basically already there. The idea that this is a… was never defined and specified. If you can detect the new sampler being used, you could say, hey, the rest of the system's using a new sampler, please consider upgrading.
… So then, then I introduced, essentially, the text that I had replaced it with as a second sampler. So now the new thing is called Probability Sampler, but I haven't changed its definition at all here. So I changed the name.
And, … Given that we were here, I had a slight change that was for the better, that the old thing was trying to keep the definition of trace ID ratio-based sampler, which included how to format your description. Since we're creating something new, we could be a little bit better with that description. So, whereas trace ID ratio-based used to just put in A decimal number that was, like, as close as it felt like it needed to be for precision.
The new implementation can be exact.
So here, for example, is… probability sampler with a 1 in 10,000 configuration, and you can exactly specify how much precision you're using now, after a semicolon. So this, so this, so these are both valid definitions for probability sampler 1 in 10,000. Just depends on how much precision you want.
So, … And then, with that, there was just one slight change to the text of the warning, but just the name effectively changing. And… … And that's it. So, it's not very big of a change, and I just wanted to describe it before I let it for you to review.
And that's it. Thank you.
I will answer questions.
**Trask Stalnaker** 39:11 For the description, I feel like it had come up in the JavaSig before, but I can't remember, … that… We were wondering why the description was even specified, like.
What's the purpose of having a… specified description.
**jmacdonald** 39:33 Yeah, I kind of agree. I know that at some point, there was a push to make the GET description not promise to be mutable, or mutable, so that the Jaeger remote could return its description that was, like, dynamic.
I do think it's kind of silly to specify the description, but, as long as we're there, it might as well be a good specification. So I would be glad to remove the exacting nature of that spec.
**Trask Stalnaker** 40:05 Does anybody remember why it was spec'd in the first place?
**jmacdonald** 40:11 if I had to guess, it's because in those early days, someone thought, well, you know, I need to know what my probability is so I can, like, do the math, and I would put… but it was so unfinished, like, what are you gonna do, read the log of of this, or implement some custom thing to report the description of your sampler? No.
And the whole point of this specification is really to say that, you know, probabilities can be dynamic, like, descript… having a description doesn't help anybody, and the point of this work is to get the probability into the trace state so that you can count each span individually, and then we can have rate-limited samplers that dynamically change, and so on.
**Carlos Alberto Cortez** 40:51 I think Yuri may remember as well. I remember him mentioning this years ago.
So, out of curiosity, I will ping him and try to, you know, get information on that.
So I don't remember, honestly, either.
**jmacdonald** 41:03 Yeah. Thank you.
**Trask Stalnaker** 41:05 I'll leave a comment on the PR about it.
**jmacdonald** 41:13 I think my… mine was the last on the agenda.
**Liudmila Molkova** 41:22 Yeah, so there is nothing else on the agenda. Does anybody want to, throw the last-minute thing in, or should we call it?
Okay.
So, following Carla's tradition, count 1, count 2, count 3… Have a great rest of your day, everybody.
**Reiley** 41:43 Thanks, Ara.
**Carlos Alberto Cortez** 41:44 Europe.
**GZ Gregor Zeitlinger** 41:46 Bye.
