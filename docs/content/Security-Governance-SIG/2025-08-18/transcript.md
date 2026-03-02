SIG: Security Governance SIG
Date: 2025-08-18
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 00:38 Good morning.
Sorry, Riley, I was… commitment to review your PR before this meeting.
**Reiley** 01:09 It's okay, I got a couple reviews. It'll be great if you can do okay.
**Trask Stalnaker** 01:17 Anything you want to talk about? … On the existing comments.
**Reiley** 01:25 Oh, so if you look at the comments, it's mainly about what's the bar. Like, people don't seem to have concern about the general direction, like, they think that's a good list.
There's some minor suggestion about the perturbation.
Which are already fixed.
The second part, which is still being actively discussed.
It's for different level of the severity. What's the response time? So.
one position, from Pablo, I think.
is, hey, like, there's a… seem to be some, like, CNCF common practice And…
People in general are saying, like, 60 days or something.
then I have a different position, because if this is the open source general practice, considering we're not the final product, we only produce some intermediate thing for other components to use. So my worry is, if we stick with the 60 days.
then other open source software, depending on us, won't be able to meet that thing, so I feel OpenTelemetry should
at least cover… The number of days, by 50%.
And depending on how things go, maybe we want to be even more aggressive moving forward.
**Trask Stalnaker** 02:40 So, what I've generally… done in our repos has what I've….
**Reiley** 02:49 Said….
**Trask Stalnaker** 02:50 in our repos, Java repos, is…
If it's high, if it's a high or higher, high or above CBE, we will release a patch for it.
Within, like, a week, But basically, it will be, you know, a patch.
Otherwise, it will get rolled into our… monthly… Yeah. …release update.
Now our monthly release cadence is… I wouldn't want to guarantee 30 days, because, like, it can be a little above or below. We're not always, like, right on time.
…
So as long as it's not a must 30 days, I mean, I think 30 days, like, as a target.
Seems fine, I…
I wouldn't want people… there's so many medium, and low CVEs, I would… I wouldn't want people to have to go out of their normal monthly release cadence for those.
**Reiley** 03:52 Yeah.
**Trask Stalnaker** 03:56 So, maybe… We can say, like, it should be…
In the next monthly release… …
But no more… must not be more than 60 days? Like, should be in the next….
**Reiley** 04:18 Yeah.
**Trask Stalnaker** 04:19 Just so that… because people can get a little…
maintainers could get a little worried, like, about the letter of the law there. It's like, oh, our next release is…
More than is….
**Reiley** 04:32 Yup.
Not quite.
**Trask Stalnaker** 04:34 Gonna make it.
Hey, Drew.
**Adriel Perkins** 04:46 Just curious, are we differentiating between, like, downstream library vulnerabilities versus our own… … component caused…
CVEs? Or are we….
**Reiley** 05:01 Combining them all together.
So, after this discussion, I… I tend to separate them, because the… the CV is in OpenTelemetry codebase.
We'll start Being a private one.
And we have the time to fix, and… and the maintainers decide when it's becoming public. The…
the dependencies, if they have CVEs, the moment OpenTelemetry starts to learn, it's already after the fact.
the upstream maintainers, they have to acknowledge the issue, they have to provide a fix, then they publish the CVE. So we know that it's already well known, and we should take more…
proactive action there, I believe.
**Adriel Perkins** 05:55 Okay.
**Reiley** 05:56 Like, I'll give one example. If we have a dependency on some critical security vulnerability that's already public, we should fix that as soon as possible.
Ideally in a week, but, like, currently we're saying we give people, like, 2 weeks.
And…
If we have a critical vulnerability, someone report that privately, and it's hard to fix, and it can take maybe, like, months for us to figure out the…
the solution. And I know in some operating system, the…
there are groups who actively study the back door, and they report the issue in private, and they give people 6 months for them to respond. So the message is, we'll give you this for, like, a bounty hunter or some program, and if you don't fix that in 6 months, we're going to make this public. So it's very generous.
**Adriel Perkins** 06:48 Yeah.
Okay. No, I was… I'm in the… I'm on the same page. I just wanted to confirm that that was the way we were thinking, that we were differentiating the two. Downstream, like, CVEs, I think there was probably one recently that I thought of, and that happens a lot, right? It's like.
just Golang version compilation, right? Just updating Golang to the latest patch release, or making sure that that's
And all dependencies require that version or greater, is a common thing that…
can be quickly fixed, usually. This is, I think, the case for, like, the collector, as an example, where we've, you know, been, building with, like, 124.7, and then all of a sudden Go itself fixes a critical vulnerability. Of course, if you don't start to compile your collector with that.
And release the latest update to be saying… to say, like, 123.8 or greater… and greater than, then, you know, that will go into downstream, things, and people will start to pick those up. Or, like, one of the standard libraries, for example, if, like, HTTP standard lib comes out with a vulnerability that has to be patched.
Because it can be culled by our codebase, which is, I think, part of… part of the determination aspect is, like.
yes, this is a vulnerability in the standard library version that we have, but is it actually a vulnerability that could possibly be executed based off of our code? You do have to kind of figure those things out, too, but it's also usually easy enough to just update the version and release a new version.
**Jeremy Corley** 08:27 Okay, this is great feedback.
**Reiley** 08:30 Yep.
**Jeremy Corley** 08:31 One of the things as well is that,
The, … even… even if our code…
doesn't use whatever piece of the vulnerability, you know, technically that's in there. I mean, that…
You can argue that gives us a little bit more time to fix.
But there's an argument that we still need to fix it, because a lot of time.
the code scanners that people are using, for corporate reasons or whatever aren't gonna care whether or not you're actually using that piece or not, and we're just gonna force people to stop using OpenTelemetry if
You know, we go, well, we don't really…
You know, use that part of the code, so therefore, you know, we don't really need to fix.
**Reiley** 09:11 So, you know, people drag their feet about that.
**Jeremy Corley** 09:14 So, …
So it's just… it's, it's an unfortunate practical consideration as well that we need to, like, stress with maintainers of…
You know, in that element, because I think it's very easy to get into that mode of, oh, you know, oh, well, you don't use that piece of the library, we don't call that function, it's vulnerable.
So it doesn't really matter.
**Adriel Perkins** 09:35 Yeah, yeah, totally. Happens all the time. But I think a lot of times, too, it's like, people don't even know if they are used or not, right? Have we given, guidance around what tools we can use here to help investigate those things?
Because, like, for example, one of the tools that I found to be really useful is what Google provides through OSV Scanner.
You can run that really quickly locally. I put it in, like, the make tools of my distro of the hotel collector, and it identifies what vulnerabilities and downstream transitive dependencies exist, and, like, whether or not they're called by any of the code, and you can use that as part of, like, your research
Aspect, where, like, hey, we've, you know, we're getting this report that there's an, you know, security
And honestly, we could probably serif push this to the repo so that code owners, like, in a workflow, could see this privately. But it gives you that information around, like, what transitive dependency issues there are, and then whether or not they're actually called. And of course, if it's not called.
You know, fine.
Still patch it in your next release, but if it is cold.
you can quickly patch it now, and you can provide both of the results when you are patching it in either form, right? Whether or not it's cold or cold. Maybe you have until the next normal release cycle if it's cold, but you can do a patch immediately if it is cold.
**Reiley** 11:02 Yeah, so, if you look at the current PR, I have a recommendation saying each repository maintainers, they should figure out what's the proper tooling, and they need to report all the dependencies.
And I… I try not to give recommendation on which tool they should use, because I believe the recommendation of the tool should be in a different repo, because it's not only for security. I'll give you an example. You want to understand all your downstream dependencies, because they might contain a license which is not a patch tool.
And you want to make sure you acknowledge, like, copyright, or the license. Like, we don't want an OpenTelemetry component to depend on another Apache tool, and eventually it's depending on an incompatible license, and believe that they have legal issues.
Right, so instead of having separate groups giving different recommendations, I hope we can give a holistic recommendation and push the maintainers to be more accountable there, because
they're more familiar with their language. Like, maybe, like, Golan would come and say, this is the best tool that we want to use, and Donate would come with, this is the tool we want to use. We don't want to dictate on that.
we want to tell them what we want to achieve, and then they can document that. So, for example, if there's a language like Golan, it's being used in the Go SDK and the collector, maybe the operator, then these maintainers, they can share the information in a common place.
**Adriel Perkins** 12:28 Yeah, I'm definitely all about not dictating
Do you feel, though, it would be nice to give them recommendations for starting points, especially for those maintainers who may be more, are less familiar with, like, well-known, good tools in the industry? And that way, they can at least have a starting point for options that they could try?
**Reiley** 12:48 We can give them example, but we don't expect us to document that in a way that it is the recommendation from the security sake.
Because it might be incompatible with other recommendations.
I remember we tried that with Icebomb, like, we give people some recommendation on how to generate ice bomb, but the maintainers later decided they're going to use a different way, and they didn't come back and update the doc. So, I feel this is not something we…
we'll be able to maintain. But putting recommendation, like, example, saying, this is what we know when we wrote the document, that seems like a good balance.
**Adriel Perkins** 13:31 Okay. Yeah, I'm not thinking recommendation as much as…
potential option for a tool, if that makes sense. Like, I think there's probably nuance in my language there.
**Reiley** 13:44 Yep.
**Trask Stalnaker** 13:46 Yeah, I tend to agree that the, the only way that we're going to get…
All 70 repos on board.
Is kind of a… give them a template, something that, like, very clear, like, do this, or go and do your own thing, it's fine, as long as it meets the…
be, … security… guidance.
… It's very… yeah. I was…
Riley had recommended looking into Trivy, I'll also.
**Reiley** 14:28 in….
**Trask Stalnaker** 14:28 to… just Dependabot.
Which seems to be, … Much better.
These days…
Not for dependency updates, but for security checking, like, it's a lot of stuff built in, and…
There is some stuff that.
**Reiley** 14:50 Like, you….
**Trask Stalnaker** 14:50 Can upload the… you can
There's a great old plugin that understands all the dependency structure, and so you can push that.
And then that is used to drive the Dependabot decisions.
… So you can see in my list of my fork, I was playing around with it, and…
It's a little overwhelming, in… this is the Java instrumentation repo.
This is where, like, there's gonna be definitely some weird repo-specific stuff.
Because, …
Right? We intentionally test against a lot of old versions for compatibility reasons. We don't include them in our distribution or production dependencies, but it's capturing a lot of these things that
we test against.
But don't actually ship.
….
**Adriel Perkins** 15:53 Right. Just one note, you probably should delete this recording since you're screen sharing that. I don't….
**Trask Stalnaker** 16:00 I think we discussed this previously, that this is all public, these are just… yeah, I'm not sharing…
Any private vulnerability reports, it's just….
**Adriel Perkins** 16:11 Okay.
**Trask Stalnaker** 16:11 Anybody can run this on their fork.
Yeah, I was trying to capture the…
a discussion earlier around, like, I… I don't think I'm saying this well, but… for critical and high…
That need to be patched.
You…
to me, you can… that should be after rescoring, like, so if there's a critical CVE and a dependency, but you're not using that part of the dependency.
Then you don't have to patch that within 2 weeks.
But for medium and low, or
You know, then it's regardless of scoring.
to Jeremy's point about the scan, we're just… at that point, we're just doing a service to
Mostly to people to quiet the scanners.
So I'll, I'll say wordy, I'm not sure about…
But I'll leave the, comment.
Cool. Hey, Tony!
Welcome, you made it, alright.
**Tony** 17:33 Yeah, so sorry, I had, somebody not necessarily respect my calendar, so… I have a little bit of a delay. Nice to meet you, everyone.
**Reiley** 17:40 No worries.
**Trask Stalnaker** 17:41 Good to have you.
**Jeremy Corley** 17:48 Yeah, the other thing about scoring there, Trask, on your point there, there's…
There's two different pieces there, because technically there's the…
CVE that the dependency may have, and then there's the CVE that we may publish for the hotel component. And those definitely can have different scores for exactly the reason they were saying, that if…
The dependency can come in with a high vulnerability,
And, because of the way that we use the library, we could either not use it at all, so we don't really need to post a CVE for, you know, our end, or, you know, or something could actually come in with a low vulnerability on a library, and for some reason, there's some complicated way that we are actually more vulnerable because of it.
and it turns into a high for us, you know, like, that kind of thing can happen, although the second's much more rare. But…
It's, it's a, … You know, but… but it is interesting. If something comes in with a high…
for a dependency, and it doesn't actually affect us, it goes back into that other bucket, and so, you know, I don't know how much we…
Need to get into that, into that description, but just in general, saying if something is… you know.
High, you know, we want a rapid fix, because, yeah, it's going to set off everybody's scanners and everything.
**Trask Stalnaker** 19:17 Yeah, we've discussed this before about… … when or if…
we want to… we should publish our own CVE if there's a… CBE and a dependency.
Do you remember if we came to any resolution or documented that anywhere?
**Reiley** 19:42 remembering how.
**Jeremy Corley** 19:43 Yeah, the record…
Yeah, and I think the recommended practice there is, if we are exposing it to the world, regardless of whether it came through a dependency or not, it is our CDE, because it is something we are sort of, quote-unquote, responsible for.
So, you know, if we have a front-end, you know.
HTTPS library or something that ends up having a critical vulnerability, and then we published
you know, hotel exposing that
In some sense, external customers, quote-unquote, don't care why we had the runner, really, that it came from a dependency, it's just the fact that OTEL had a high vulnerability dependency on its bracket.
So we really do need to… Publish in that case.
Or we should.
I should say.
**Trask Stalnaker** 20:30 Okay, so kind of similarly, if it's high or above.
After rescoring, then we should publish our own CVE.
**Jeremy Corley** 20:42 Right, I mean…
Technically, you could argue that even, you know, lower scores, it just depends on how much we're really gonna care
you know, … You know, if there's a low, and… This, you know.
how much responsibility do we feel with that? In theory, again.
we really should be publishing our CVEs, you know, in general, but it's just…
But definitely for things like high and critical.
I couldn't get.
**Trask Stalnaker** 21:22 Yeah, it would be interesting to… So the reason I, ….
**Reiley** 21:28 I….
**Trask Stalnaker** 21:29 hesitate to make this recommendation, even though I totally agree with you that, on the right thing to do.
is that… There's so many… at least in the Java world, there we see so many…
medium and low severity, CVEs in our dependencies.
And… Even to do the analysis on those, to understand if they are being used and exposed and, …
… Is a lot of work, and so it's so much easier just…
Bumped the version, release the, you know, the next monthly release.
**Jeremy Corley** 22:15 Right.
**Reiley** 22:17 I shared a link, so if you look at the chat, the second link I shared is what we discussed before, so we captured that in a doc.
And one key thing that I think we talked about is for executables and libraries, we have very different opinion.
So for executables, our goal is we want people to use an executable when they run a scanner.
there shouldn't be CV, that's the ultimate goal.
And because people don't have the control, so if….
**Trask Stalnaker** 22:52 Right.
**Reiley** 22:53 We have a critical CVE in the dependency, although we've done analysis, we're saying we only use serializer, there's a deserialization code path we don't use, and that thing has a critical CVE. We don't want to defer that, because people are using that
They might have some compliance reasons, like, they might have scanners, so they have a policy that would prevent them from eating this.
For libraries, the bar will be much lower than executable, because in libraries, our general recommendation is you don't specify a particular version. Instead, you specify a range.
So, the lower part of that range
hasn't seen it yet, but people who
use the library to build applications, they can still
Explicitly specify a higher version to mitigate the issue, so they have the control.
Cool, yeah.
**Trask Stalnaker** 23:50 Yeah, this is great. Yeah, I'm glad.
**Reiley** 23:51 So in this case, like, if we shape an executable, like collector, then if the collector has an underlying dependency, like a…
a serialization and deserialization library, and that deserialization part has a critical CVE. I think the collector would… would do this. The collector would say, this is a critical CVE, we should patch that following the critical CVE timeline. But we're not going to publish a new CVE, because that's not affecting the collector.
**Trask Stalnaker** 24:25 Cool.
Yeah, this is good stuff.
**Reiley** 24:30 Yeah, sounds like I need to put some examples here, because a lot of things we discussed, like, we put a lot of…
Ideas behind this, but…
over time, it's becoming very tricky. A lot of people, without the contacts, it would be hard for.
**Trask Stalnaker** 24:44 Yeah.
**Reiley** 24:45 Why we're doing this.
**Trask Stalnaker** 24:47 That's a good… that's a good… Idea.
**Reiley** 24:51 Okay, I'll add some examples.
Okay, so I'm down for this topic.
Thanks, Ara.
**Trask Stalnaker** 25:20 I… have kind of an ongoing topic, but I haven't done any….
**Reiley** 25:27 work.
**Trask Stalnaker** 25:28 On In the last 2 weeks, so… That will be… I will… But it's still on my… …
On my docket, for the… let's see… Yeah.
For just, kind of, the… the…
Practical recommendation corresponding to, this is… this is the rule, and then… having some…
Guidance for maintainers who just want to start somewhere, anywhere.
….
**Reiley** 26:09 easily.
**Trask Stalnaker** 26:17 Cool, anything else that… To chat about today?
**Jeremy Corley** 26:24 I, I had, one thought, on the security alias, because I, you know, I think last week we got somebody that came in, and thanks for answering that, Charass, because that's…
what, I, I was… I was thinking of pointing them to the, … …
to the publishing and advisory thing on the website repo, but it was one of those where it's like, oh, I should… I wanted to…
send something out between us to discuss it first, and I realize that we have some, …
sort of backdoor ways of doing that, but I was wondering about a communication mechanism Between, you know, us.
you know, sort of maintainers and, approvers within the security SIC.
Do… do we have an official mechanism for that?
Like, if we… if something comes in like that, and we wanted to sort of discuss it officially between everyone who's a maintainer and advisor…
Or, approver.
**Trask Stalnaker** 27:28 Do we feel that Slack…
is… I mean, I would say Slack, unless there's concerns about Security there, but….
**Jeremy Corley** 27:38 Okay.
**Reiley** 27:40 Yeah, I'm fine even in Slack.
**Jeremy Corley** 27:42 Okay.
**Reiley** 27:43 Trask, are you sharing? Do you have a…
You have a blank screen, I think. Something maybe protected.
**Trask Stalnaker** 27:50 Oh. I see a big….
**Reiley** 27:52 green box.
**Trask Stalnaker** 27:53 That's interesting. Slack is… I mean, Zoom is doing it different now when you bring up a window on top.
It used to continue sharing the window underneath, I thought.
**Reiley** 28:06 Okay. ….
**Trask Stalnaker** 28:07 But yeah, now it's giving me a message, please move this window away.
… Yeah, why don't I create, … do we care who… if it's… it's not…
Yeah, the Slack channel doesn't need to be owned.
Yeah, why don't, Riley, why don't you create the Slack channel?
… Just since you're the most permanent member of the maintainer group?
… And… Yeah, I would say just add… Do we…
Who do we have in the security… alien in the… Oh, we did 3…
Oh, what do we have? Sorry.
**Reiley** 29:04 So I'll see how to fix that. I think we have one, but there…
There are members that we need to remove.
**Trask Stalnaker** 29:14 Okay. Yeah, I would say just sync it to whatever… whoever's in that security at OpenTelemetry I.O.
**Reiley** 29:22 Yeah. With the right group.
Yeah.
**Trask Stalnaker** 29:26 Awesome.
**Reiley** 29:34 Okay. Alright. Here we go.
**Trask Stalnaker** 29:37 Yeah. That's fine.
Bye.
**Reiley** 29:40 Go on, bye.
