SIG: Communications SIG
Date: 2026-03-31
Duration: 18 minutes
Zoom Recording URL: https://zoom.us/rec/share/1lafMO24poPYzbRbfliR7_8YXNfeV7MTezUp-M_EO95_pHnI_QoaePhVgEugH19R.hr4hbKNrXhi5VnmJ
============================================================

## Zoom Recording Transcript

**Tiffany Hrabusa** 00:53 Hello, everyone.
**Jay DeLuca** 00:55 Hello.
**Diana Todea** 00:59 Hello?
**Tiffany Hrabusa** 01:11 Since we had.
**Vitor Vasconcellos** 01:13 Oh.
**Tiffany Hrabusa** 01:13 A little bit of technical difficulties this morning. Well, my morning.
We'll give everyone another minute or two to join before we get started.
Okay, I see we have, a couple new folks here, so I'm going to paste the link to our agenda document in the chat.
If you have anything that you would like to… Discuss, you can add it there, and you can also add your name as an attendee if you'd like.
And… I think… I think we're good to get started. So, Diana, your first stop.
**Diana Todea** 03:30 Okay, yeah, I think Patrice is not here, right? Right? He's on… Parental leave? Yes.
**Vitor Vasconcellos** 03:40 He… he's not joining today.
**Tiffany Hrabusa** 03:44 He's… yeah, he's, he's working his way back, he's getting caught up.
So, we… The… the meeting thing is… Yeah, it might be best to wait, but you can also raise it in the comms channel as well, and we can maybe work on it async.
I do think that it would be… Helpful to have, something like that, even for, contributors who aren't working on localizations, just to understand the CI and the build process. It would be nice to have a recording that we could refer people to if they want that kind of resource, so… I don't think we'll make any progress on it today, but, I do agree that it's, a good idea, and Once everyone's back.
on board.
Then we'll, make some progress, hopefully.
**Diana Todea** 04:47 Yeah, I mean, it was more like… Obviously, we can discuss even now if you want to, but if not, we can wait. I'm not sure, it's like, I cannot join all the meetings, and… everybody's pretty busy, but yeah, I mean, what I wanted to understand besides the triaging part, which, you know, looking at issues, trying to think, like, how we're basically triaging. If there's something else more useful, like, not more useful, but more relevant, meaningful, you know, that I can do besides that. I'm open to suggestions.
maybe, what was your experience? Did you do anything in Plus? Anything like that? Obviously, and I'll try to fit it in my… Free time?
**Tiffany Hrabusa** 05:38 Okay, yeah, I do think… doing as much of it async, so if you have specific questions, maybe, noting those down in a thread, so that we can figure out how to address them, either in a meeting that we record, or maybe these are things that we should flesh out more fully in the actual contributing documentation. So, having your specific questions would be… would be helpful.
And I think given, as you said, everyone's time is… is constricted right now, doing as much async, is…
**Diana Todea** 06:19 Yeah, no, this is a direct question, sorry. So, my direct question is, I don't have… I mean, when I have triaging questions, I will ask them, but, like, more from your experience going through the same, let's say, path, did you do something in plus besides that, or just… looking at the queue and trying to triage things. Is there something more meaningful that I can also do, besides that, that will help me understand a bit more all the architecture, this infrastructure of the repo. Yeah, I feel like I could do more in that sense, so if you can reply now during Today, that would be great.
**Tiffany Hrabusa** 07:02 If anyone else has thoughts, please feel free to chime in.
I… from my perspective, I learn workflows and, the… the… like, the big picture, just from, like, subscribing to the repo and reading comments on all the issues and PRs.
it gets a little noisy with the notifications, but that's how, when I was ramping up, that's how I learned, what kinds of things, were acceptable, what kinds of things that we, would say are not a good idea, that kind of thing.
it's not… It's not very, like, stark. Like, you can't say, yes, this is good, no, this is bad.
there's a lot of gray area, I guess. Anyone else, please?
**Vitor Vasconcellos** 08:04 Yeah, regarding the infrastructure part, and all the… the workflows and the setup in general. We are actually trying to write some docs.
under this… Slash site section that is supposed to be internal docs, or for everyone who's working behind the docs.
But this is something… This is a newer section, and we don't have everything yet.
Something we were doing… by the end of the last year, and I think we could perhaps try To… to keep doing that was the maintainer sync that we were doing with all the maintainers, especially after Marilla and I joined the team.
And… perhaps we could… I don't know, we could schedule some extra sessions, and this was something that Patricia always had some great… Insights, some great material to share with us.
And I feel… I feel like this is a good opportunity to… to… to have those… those sessions again.
**Tiffany Hrabusa** 09:31 I agree. Okay.
So… As far as your role as a triager goes, Diana, the most helpful thing you can do is respond to new issues.
And basically.
the response should be, do we have enough information to make a decision about the issue? So, if there's not enough information, then you can ask that question. You know, you can say.
Can you… can you elaborate a little bit more on this so that we can, push the discussion forward. And then, tagging the appropriate groups. And I think, also labeling, right? That's… that's our new thing, which is spelled out in the docs pretty clearly, I think. So… Those three things. So, just vetting the issue to make sure that it has as much information as possible.
tagging any, approver groups across the hotel ecosystem that would need to be involved in that issue, and then adding labels. So there's… there's triage labels for for, deciding, accepted, like, all of that kind of stuff. So, As a treasurer, that is your primary role. For, CI stuff.
I honestly think everybody could benefit from learning more about that. It's really… it's gotten more complex, even since I joined, and it's… not always straightforward. So, yeah, we will, like I said, not be able to cover that today, but we will work on, getting something, like Vitor said, either setting up Like an, not so much like a community-wide meeting, but more like a, I guess, approver… triager, approver, maintainer, same kind of thing, where we… where we cover that kind of stuff.
Okay, did you have anything… anything else on that?
**Diana Todea** 11:44 No, I think, yeah, I mean, I think that would be helpful also in terms of, you know, there are probably different expectations and different, you know, motivations for, anyone, you know, so that's why I think, how you say the knowledge transfer might flow a different, wave from person to person. But yeah, I think at least personally, I think that would be very useful, you know, to… besides the comms meetings, to have more, like, like you said right now, sort of, like, maintainer, and down the line.
type of meetings, yeah, I'll be more… Yeah, useful in terms of knowledge transfer, perhaps, yeah.
**Tiffany Hrabusa** 12:28 Okay, great. We will… Yeah, we will carry this forward to the next meeting, and we'll definitely, keep it on the agenda.
Okay.
Jay, it looks like you're next.
**Jay DeLuca** 12:44 Yeah, so a while back, I had, come with Jack Berg and presented, some work that we were doing on some dynamic documentation for a declarative configuration. And at that point, we kind of got the go-ahead, so I've been working on Tidying it up and getting it ready, and the PR was getting really big, like, because there's… there's an automation component from syncing, some of the schema information directly from the repo, then there's the generation of two pages, and then there's a lot of JavaScript on top of it.
And so I was getting to the point of finishing the implementation, but the PR was getting really big, so I figured I would create a tracking issue instead, and break it up into some smaller pieces, and then submit those, kind of, iteratively. So, I just wanted to give a heads up, really, that, that's kind of my plan, is, I'll probably be submitting some smaller PRs over the next couple weeks that kinda… Chip away at this, with the end goal being that we have these two dynamic pages, but…
**Tiffany Hrabusa** 13:49 Okay, that sounds good to me, and as a reviewer, I thank you.
**Jay DeLuca** 13:55 Yeah, I felt getting guilty as the lines of code started getting into the thousands. I was like, this is inhumane.
**Tiffany Hrabusa** 14:05 okay, I don't see anything else on the agenda, so… Maybe we'll do… Uzo, I see that you are here as a newcomer. Would you like to introduce yourself? Or if you have anything to say, please feel free to speak up.
**Uzochukwu Winnie** 14:31 Bye!
good day. I'm Winnie. I'm working with Prometheus LFX mentally. I'm quite shy, I don't know how else to introduce myself. Well, yeah, I'm just joining in to listen to the conversation and try to see what's going on. So yeah.
Okay.
**Tiffany Hrabusa** 14:53 Okay.
Thank you, and welcome. We are very happy to have you here.
And as Jay said, we've all taken a look at your blog post, so yeah, you're off to a great start. If there's anything specific that we can help you with, feel free to post it in the chat, or speak up, or you can add it to the agenda as well. But we're happy to have you here.
You're welcome.
Now, does anyone else have anything that they would like to discuss?
Okay, I don't have any, Updates on the collector docks refactory.
I'm still getting caught up after QCon, but I'm hoping to, get… make some progress on that towards the end of this week, and Sophia, your PR is on the top of that list.
One thing I do have an update on, the Hotel Blueprints project is moving forward, and I have a PR up to, create the new section in the nav for guidance and architecture.
So if anyone wants to take a look at that, the first blueprint is… nearly ready to be published. It's still in Google Doc form, but once the scaffolding in the website exists, they'll raise a PR to publish it in that section.
And, prior to KubeCon, we published the first in a series of blog posts with reference architectures.
I believe it was… the case study was Mastodon?
And we are going to transfer… there's a series of 4, maybe 5?
planned, that are… those posts are being, created by the developer experience SIG.
the plan is to basically copy-paste those into the reference implementation section of the new reference implementation section of the website. So, the first one of the reference implementations is ready, and the blueprint… first blueprint is almost ready, so… That is exciting.
And hopefully, the next time we meet, we'll actually have some things published.
Any other updates, comments, questions?
Okay, I'm gonna take that as a no.
So, thank you all for bearing with the Zoom issues this morning, or today, sorry. And, we'll see you in two weeks.
**Diana Todea** 17:52 Thank you. Bye-bye, Anne.
**Tiffany Hrabusa** 17:54 Bye.
**Vitor Vasconcellos** 17:55 Zero Fire.
