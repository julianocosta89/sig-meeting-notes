SIG: Communications SIG
Date: 2025-12-09
Duration: 45 minutes
Zoom Recording URL: https://zoom.us/rec/share/H4G9I9vATwmRQ-CMKdVvZp0dcwTkR_WntrfGgmd-VYUBC3v3VBQ7uvPiEfEkklZ9.zmqHdWvxzHVi6Vx-
============================================================

## Zoom Recording Transcript

**Vitor Vasconcellos** 02:08 Thank you.
Hey, how's it going?
I'm gonna find somewhere.
**Jay DeLuca** 02:14 Good, I like your shirt.
**Vitor Vasconcellos** 02:17 Oh, yeah!
**Jay DeLuca** 02:19 I got, some swag on, too.
**Vitor Vasconcellos** 02:21 Oh, yeah, that's… yeah, I wanna… I wanna think… I will have some t-shirts, Oh, it's not here, but yeah, I have the gray one.
**Jay DeLuca** 02:33 Nice.
Hey, Tiffany.
**Vitor Vasconcellos** 02:37 I hate it.
**Jay DeLuca** 02:40 How's everything going?
**Tiffany Hrabusa** 02:41 while doing…
**Jay DeLuca** 02:43 Good.
**Tiffany Hrabusa** 02:46 It's getting cold here, though.
**Jay DeLuca** 02:49 It's no fun.
**Tiffany Hrabusa** 02:49 I just saw some of the tech writers were saying that it's, like.
in the teens in Massachusetts, so, yeah.
**Jay DeLuca** 02:59 Yeah, my heat was finicky this morning. I was struggling to keep up, so I have to have somebody come look at it tomorrow. I just had a big part of it replaced a couple weeks, or, like, a month ago.
Ugh, not fun.
Hey, Maria, long time no see.
**Marylia Gutierrez** 03:14 Hello!
**Jay DeLuca** 03:17 You got, Grafana swag on, too?
Next slide.
**Marylia Gutierrez** 03:20 Yeah.
**Tiffany Hrabusa** 03:23 Feeling left out.
**Leandro Caracciolo** 03:26 Oh.
**Marylia Gutierrez** 03:27 Yeah, it is cold here. I was… I was awake of some… so much warm.
No, yeah.
**Tiffany Hrabusa** 03:36 Hi, Leandro, welcome.
Should we wait another minute or two to see if anyone else is coming?
**Marylia Gutierrez** 03:47 Yeah, I know that Severin's gonna join in, like, 15 minutes or something, so yeah.
**Tiffany Hrabusa** 03:52 Right.
Okay.
Jay, are you hoping that anyone in particular comes today?
I mean, are you waiting for anyone, I guess? No? Okay.
**Jay DeLuca** 04:07 Nope, no, yeah, I'm not sure that anybody other than who's here, my friend Mike, I didn't hear back from him about whether he was gonna show up.
Pablo… Let me ping Pablo.
There's no… there's no, like, real important reason for people to show up. I was just gonna kind of do a little bit of a introduction and a kind of a soft kickoff, but Yeah, I'll ping him anyway.
**Tiffany Hrabusa** 04:38 Okay.
Going into… Oops.
Leandro, do you have access to the meeting notes? If not, I can pop the link in the chat.
**Leandro Caracciolo** 05:06 Yeah, have assessed, thanks. Okay, great. Okay.
Thank you very much.
**Tiffany Hrabusa** 05:16 Okay, I think we're coming up on 5 after, so… We can get started, Jay, whenever you're ready.
**Jay DeLuca** 05:26 Did you say that Severin was gonna… like, he is, I guess, he's someone that I would, like, I don't know if there's other stuff that can be talked about for… I could certainly go, but…
**Tiffany Hrabusa** 05:36 Okay, if you want… Severin said that he would be about 15 minutes late, so, I can give a very, very quick update on the collector docs refactoring.
While we wait for Sovereign.
So, it's been… Little… bumpy, I would say. This first phase.
I thought I was starting with, like, a low-hanging fruit, but it turns out that I didn't plan as I thought I did.
So, I think we'll still make the deadline of the end of the year to finish everything off, but my… So the first phase was moving pages and copy-editing pages that did not require any new content to make sense, right? That was the first phase.
So just breaking up bigger pages, and shifting things around, and copy editing.
Because a lot of those pages haven't been touched since they were first written, probably before there were any tech writers working with OTEL.
So… I created issues and labeled them accordingly, and we have got several new contributors who've put up PRs for them.
a lot of, AI assistants in these PRs, so it's been tricky To know how much effort I should put into reviewing them. I think it was, said pretty well in an issue that Severin referred me to, or a PR in the community repo, but If… if it's a contributor doing the work, And… the PR needs a lot of help, you feel comfortable offering that help, like, writing guidance about how our style guide works, and how we think about this, and, you know, maybe we should do this here, and you spend a lot more time reviewing that PR to help the person, understand.
But if the PR is mostly AI-generated.
how much time do you spend? Like, do you… do you educate the author about what… about the changes that you're requesting, or changing, or suggesting?
Or do you just… Make the suggestions and move on.
Do you just… if it's copy edits, do you just… merge it, and then fix things later? Like, it's… there have been some questions that have arisen with this first phase, so… I think the one thing that I'm definitely gonna do for Phase 2 is scope the issues much smaller. I'm gonna make… like, right now, some of these pages are just very, very long, and it makes reviewing them Super, super time consuming.
So I'm gonna just make sure that, each… each issue is scoped to a very narrow window, and, Hopefully that will make the review burden A little bit less.
And… I'm still not totally comfortable with how to respond to the AI question. If anybody here has thoughts about that, I would actually really like to hear that, because… my… the struggle I have is I want to welcome these new contributors, right? Like, we need people who want to contribute and who want to stick around.
But… It's also not sustainable for us as reviewers, to… Constantly be correcting something that… took the… the author of the PR probably a couple minutes to plug into an AI and have it spit out the PR.
And then… here we are. So, I'll shut up now if you guys have any thoughts, I would really like to hear it, so…
**Marylia Gutierrez** 09:49 So I can give a few examples that there was a period that it was happening a lot on, like, the Portuguese localization, but the things, like, you can clearly see that the person… so they were both, like, Portuguese speakers and non-Portuguese speakers. When they are not Portuguese speakers, you can clearly see, and then we kind of, like, nurse them, like.
Look for an area that you would actually understand, and we just kind of close, because it's… is too much that we have to do it, when it is generated by AI. So there are a few cases that were, like.
Couple things here and there, so I just gave… you put the comments, and then they can fix it, and that's it. But there were cases that you can see that the person did not review, like, at all what was generated.
Because you start to review, and, like, I'm gonna put comments on almost every single line, so I kind of, like, stop and say, like.
It's okay if you want to use AI to create, but review before you put it up. So, basically, I say, like, take a look at your PR and make the fixes yourself, and then mark that it's ready for review.
there were people that then just disappear, so I just closed the PR, and that there were people that actually made the fixes, and then you can review on top of that. But making it clear that we are expecting you to review first whatever you generated before asking us to review. That is… has been the reply that we have been giving there.
**Tiffany Hrabusa** 11:21 Okay, yeah.
I think I'm going to have to start doing that. I even… so there was a PR that, got put up, I think, in the last couple days, and… the author just… so we've added that template, right? The PR template, where you have to check the boxes.
**Marylia Gutierrez** 11:39 Yeah, it was Love Mars.
**Tiffany Hrabusa** 11:41 No, they just deleted it from the template. It wasn't even in the PR description. And so, I was… so I commented, and I was like.
or I was going to comment, I don't know if I actually did, but I'm thinking, like, I just want to ask this person, why did you delete the template? Like… That… yeah, I don't know.
**Marylia Gutierrez** 12:01 Yeah, in that case, you can… I would comment and say, like, please, if this was created, keep the thing and mark, because maybe on their mind, like, oh, it was not here, so I didn't mark because it was not here.
But, yeah, he was there.
**Tiffany Hrabusa** 12:16 Yeah, I mean, if they… I mean, I don't know how that works. If… No, it should still, because they're raising the PR in the comms repo, so even if even if it's an AI-created PR, it should still have the template, right?
Like, if you have… if you have, cursor.
like, create the PR for you, it should still have the template in it, right?
**Marylia Gutierrez** 12:46 Because if they are having some, like, create the script and put this on the description, their script could be, like, just deleting. Because the template, what that does mean is just, like, when you click, it has things there, but it… even, like, for example, the JavaScript has that, like, fill this, fill that! I just delete all of that and put the things that are relevant for mine. That… nothing stops people from just deleting, so if it is a script generated, they could just, like, sing, like, replace whatever's there for my own thing.
**Tiffany Hrabusa** 13:22 Okay, that's something to think about, too.
**Jay DeLuca** 13:31 It's tough. We're dealing with this in Java, too.
just, drive-by PRs, where it's very low effort. It's hard to know whether a person was involved at all. But… Yeah, I think it's a fine line between discouraging people from Contributing and participating, But I think, like, so we're just in the process of adding the PR template, as of right now, to have, like, the disclosure of, like, how much AI did you use here?
I think that's a good step, but it doesn't solve… still the problem of, like, the asymmetrical effort of, like, the reviewers and the PRs.
I… honestly, I don't have a great answer. I think… education or, like, disclaimers are, like, the best we can do right now? Maybe… we could use Copilot to… I… I don't know if there's a way that we could have Copilot identify low qual… like, low-effort PRs, and have it coach the person of, like, hey, it looks like, you know, this is very ambiguous, or, like, maybe it didn't hit the mark, could you please show your work, or… Something else that kind of puts a little bit more of the… the effort on the… The contributor of just, like.
Not, like, prove that you know what you're doing, but, like, provide a little bit of a paper trail or evidence to be, like, this is… like, to help along the reviewer.
But yeah, I think in general, this is just a really complicated… problem.
Especially in the dock stuff.
Oh.
**Tiffany Hrabusa** 15:18 Yeah, because…
**Jay DeLuca** 15:19 I guess people see it as a lower barrier of entry.
**Tiffany Hrabusa** 15:22 Exactly, and we want people to come into the community through docs, like, we want that to be the case.
**Jay DeLuca** 15:26 It's…
**Tiffany Hrabusa** 15:27 But, Vitor, I was just going to ask you.
Didn't Patrice say something about there was some kind of tool in another open source repo where they were using AI to assess how much AI was being used in a PR?
**Vitor Vasconcellos** 15:44 Yeah, yeah, we had some alternatives to, like.
calculate the high score of the possibilities of being something related to that. I think it analyzes the content and the description for that PR.
We… we can try that, but… Wow, that, that will… mark the PR, like, show us a warning, like, there's possible GenAI comment here.
**Tiffany Hrabusa** 16:18 I mean, I think that.
**Vitor Vasconcellos** 16:19 Yeah, we…
**Tiffany Hrabusa** 16:20 consider that, because if what's happening with, like, I don't know what agent or LLM they used, but, like, if it was Cursor who created that one PR I saw where the template had just been deleted.
then, you know, they're not acknowledging it. Maybe having the score would force them to acknowledge it in some way? I don't know.
I don't know.
I guess I'm kind of thin-skinned about this, which is my biggest problem, is I don't know how hard to push back.
And I don't feel comfortable pushing back all the time, and so I end up taking the burden on myself to just review these PRs.
And it's… it has not been a pleasant experience. So I've been taking, like.
5-day breaks between touching these things, because I just… for my own sanity, I can't… I can't look at them every day.
All day.
Anyway, Severin should be here shortly. Leandra, did you have anything that you wanted to talk about?
**Leandro Caracciolo** 17:25 No, I'm just listening to this and trying to understand how things work. This is my second meeting, so I'm just trying to listen and understand it better.
**Tiffany Hrabusa** 17:36 Absolutely. We're glad you hear… you are here, and you are hearing all of our… wackiness.
**Leandro Caracciolo** 17:44 Let's hear first.
**Jay DeLuca** 17:52 Oh, should we just get into the Ecosystem Explorer?
**Marylia Gutierrez** 17:56 Yeah.
**Tiffany Hrabusa** 17:58 I think Severin should be joining us very shortly, so…
**Jay DeLuca** 18:02 Cool. Let me, share my screen.
So I put some… some notes to… down, just as a… kind of an outline, but, I think everybody, maybe, Leandra isn't familiar, but essentially what I'm going to be talking about is, We recently had a project proposal be merged within the community repo that kicks off something that we've been discussing for the past 6 months or so.
Around, basically, leveling up our documentation around specific components in the ecosystem. So, right now, we have the documentation site, which has some great high-level, things around the specification, how to set up Java agents, some configurations, things like that.
But what, is missing is more detailed, information around, like.
what metrics are omitted, what spans are omitted, what is the metadata… what are the attributes associated with them? For various configuration options, what changes if you do them, things like that. So, it's kind of this very nitty-gritty, detailed.
data set that, we don't have yet anywhere, and even if we had it, how do we display it? Like, what is the user experience for being able to navigate that type of information?
And so, I've put some thought into it around, basically.
taking some structured metadata and then building some UIs on top of it that allow people to do things. And so, we have this proof of concept here, where you can go into a particular instrumentation, you can see what configuration options are available, what versions of the libraries are, use this instrumentation, and then things like metrics and spans and have information, you can see the differences between different versions. So that's… that's kind of the high-level background to… to what this project is. And so… While we've been, creating some proof of concepts, and having some discussions.
we have the… the project is merged, and so we kind of have the green light to… to kind of move forward with this under the OpenTelemetry umbrella. And so we're going to do this within the context of the communication SIG, seeing as it's very documentation heavy. And so, you know, some of the goals of the project, in general, are, like, the way that I look at it is, like, automated documentation. So the goal is, we have all this complex information.
that we need to keep up to date, and we need to make it available and discoverable to users. And so, the places that we're gonna start, at least our primary focus, are going to be, Collector.
And so, the scope for this one's a little bit smaller. The collector already has metadata, and so the task that we're going to tackle as part of this project will be to use that metadata to create some automated pipelines to generate documentation and to update the existing registry. And a subnote is that Tiffany is in the process of reworking the collector documentation, so just identifying areas that we can basically streamline and hook in. And so the idea is that The underlying metadata and information can be maintained by the maintainers of that code alongside their code.
And then we have, like, a separate process that then collects and aggregates all that information into some kind of centralized place. And then we have, kind of, automation that builds off of that and takes that information and then updates things, pushes things out, transforms that data into other shapes, whatever.
And so… so yeah, so one of them will be to continue the work on the collector. Pablo.
I reached out to him, he wasn't able to make it, but he's been on board with that, too. So, I see this kind of leg of the project to be kind of guided and informed by Tiffany and Pablo, but I have been in the process of kind of figuring out how the automations work and that kind of thing, but certainly looking for others if they're interested in helping there.
The second goal, at least from the way that I'm looking at this project, is basically a productionized version of this. So, I've been experimenting with ways that we can do all kinds of stuff, whether it's through configurations, whether it's Analyzing a dependency tree for a service, and then giving all the information that… we have all kinds of ideas for this, so the… one of them is to kind of identify what the core set of features will be for the Java agent documentation, and build out that full Ecosystem Explorer website, specifically for the Java agent. We also want to expand that, like, I think that it's very possible for us to do a similar model with the collector, since we already have this metadata, and so the idea will be we'll kind of do things in parallel. We'll update and populate and maintain the existing V1 registry with this information as part of this project, while also exploring this new, UI aspect for the same information, but potentially more powerful ways to slice and dice it, and get involved.
We also have someone from the Golang SIG, or… or… he's not… he's not a maintainer or a contributor or anything, but he's someone interested in that area. And he's doing some exploration of how we can generate the metadata for Golang, so that's another one that we might be able to pilot. And then JavaScript already has a lot of this information, in READMEs, and so I want to explore converting those READMEs into metadata, and see if we can… how far we can get along with that as well.
So, so this one, you know, has the other, so the collector, Golang, and JavaScript, as well, as far as we can get.
And then the third kind of pillar of this project is… and maybe this should have been, higher up, but it's basically the central database of this metadata, that tells us about all the different instrumentations, or components, or… Or whatever. And the thought there is, if we have this, you know, centralized I call it a database, but I don't know what it's going to look like, whether it's just some kind of registry or however you want to think about it, but basically taking all of this information that we have across all of these different projects, whether it's the languages or the collector.
and centralizing them in some format that can be used by tools, or LLMs, or whatever. And I don't necessarily mean that we, like, host a database that people can actively call into.
But more along the lines of maybe we just have, like, a published artifact somewhere where they can download, like, a SQLite database, or whatever that looks like, and then plug that into other things. And maybe we can host it and make it accessible to other things. Like, for example, I can imagine you know, maybe the existing documentation site being able to leverage, you know, a data store like this to do more things. So that's kind of the high-level goals, and still, this is… this is all very fluid, and, over the course of the next month, I'm going to try and distill a lot of these things down into, like, some documents that we have as kind of, like, a, you know, a project description and all that. I know we have the community doc, but we'll have some more, kind of.
Stuff that we update more frequently.
Any questions on any of these, high-level goals before I talk about where we're at as of now? And Severin, welcome.
**Severin Neumann** 26:23 Yeah, hi.
Sorry for being late, but yeah. No worries.
**Jay DeLuca** 26:30 Anybody else have any questions on, the goals?
Cool. Alright, so where we are. So, since the community project has been merged, we have a project board. It doesn't have much on it yet, but that's another thing that I'm gonna work on over the next month.
We have some GitHub teams now, so we have, an approvers, and we have a maintainers. Not that they're assigned to anything or anything, but, you know, it's great, we got the… a little bit of momentum there.
you know, there's… I think in terms of the mechanics and stuff, at some point we'll need a repo, but I don't think there's a huge rush on that right now. I have some other things that I want to plan out first till we decide what that means, whether we'll have one repo or if we'll need multiple, but that's kind of, to be determined.
So then if we talk about where we're at with some of the actual work, like I had mentioned, we've been… we've been hacking away at this for… I think I've been… I started work on this on a… not in the same context, but I've been working on the metadata piece since March of this year.
And then we've had some discussions and other things along the way, so… so we're not starting from zero. So for the metadata itself, so, like, the source data, and… and this piece is technically… Outside of the scope of this project, I have a diagram, let me pull up.
That kind of shows what I'm thinking here.
In terms of what is in scope and what is out of scope.
this is just a quick diagram. So, the metadata… defining metadata definitions, so, like, whether people use Weaver or whatever, actually creating the metadata is… we're gonna say it's sort of outside of the scope of this. We'll certainly be doing work there, but, like, this project itself is really focused on synchronizing, collecting, aggregating this information, and then building on top of it.
So, for the… that first piece, that metadata sources, we already have… Java, so like I said, I've been working on that since… since March. I would say I'm about 60-70% done with going through and… basically identifying all the, needed information for the 260 different instrumentations in that project.
We have… the collector already had metadata, I think it might be still evolving, but it has enough for us to get started, and we will continue evolving it as needed, like.
For example, we recently… we're adding display names, things like that. And then we have some Golang experimentation, and then in the future, we might be able to do some… some JavaScript stuff.
So that's kind of the current state of the metadata, and so I'm gonna… I'm continuing to drive this. My goal is to have this done by, like, end of January for Java, and then I'm not sure about how quickly we'll be able to jump on these things, but I don't think there's too much of a rush. As of right now, there's plenty of other work to be done.
And then for the metadata collection and the data aggregation.
So we have a proof of concept in place for the collector, which basically, every night aggregates any changes, and then after every release, it will basically synchronize all of the documentation related to those, components or any changes around stability, things like that, added or removed components. It's all working pretty well.
I've just been kind of working out the kinks each time there's been a release, but I think it's pretty close to being ready to… move into, like, an official repo, or however we want to do that. But, yeah, so that's… that's kind of in a good place. We have a POC in place for Java as well.
And, I think that will evolve as well, but, you know, we got enough to do some stuff with. And then we have some documentation automation, so I have a couple jobs that are doing some of the Java stuff, both for the Explorer, but also for the documentation site, standard pages. And I'm gonna continue to do some more on that.
And then, like I had mentioned, we automated some of the collector component, pages, so far.
And then for… so for next steps, so we just got the… the project merged, Severin's working on getting some of the, you know, or already did work on getting the… the pieces created, so what I'm gonna focus on, you know.
we're in December, there's holidays, time off, I think even Pablo's off for, like, the next 2 weeks or something. So what I'm hoping to do is take the next few weeks to really start hashing out some of the planning and creating some more… tickets in the backlog, and kind of hone down what I think to be the MVP feature list of things we want to focus on short-term that are like, we definitely want to do these, versus things that are a little bit more… up in the air about, like, how we might implement it, what languages might do it, things like that. So, I'm gonna start, building out that backlog, and then… Try and come up with just some really soft… Timelines and milestones in terms of just, like.
something for us to shoot towards, as, like, a guiding light.
But yes, that's pretty much all I got, but I just wanted to use this as an opportunity to do, like, a… like I said, like a soft kickoff, and just… Do a little bit of a brain dump, but, yeah. Anybody have any… Thoughts, questions?
**Severin Neumann** 32:30 I mean, all I can say is that I'm excited. I mean, just to throw this in, logistic-wise for this meeting, of course, we have to figure out, like, depending on how much time this is going to consume in the future, just for everybody also to have this concept, this context.
like, we… Jay and I, and I think with the maintainers, I talked about that, we want to have this meeting as part of comms initially, but if over time we recognize, like, hey, more than 20, 30 minutes every time we meet is consumed by the ecosystem Explorer.
then, of course, we carve out and maybe do it, like, in the alternating weeks where we don't have a meeting right now, but… but I personally think, like, having this, like, embedded right now is better than just having a meeting that only Jay and I, or whatever, two people attend, and then, like… and it's very close to what comms wants to do, right? A lot of the things that that project is going to build is very close to what our website is going to consume. So, yeah, that's my five cents.
Tiffany.
**Tiffany Hrabusa** 33:39 I was just gonna say, I'm super impressed with how much you've already… completed, and I am also really excited to see where this can go.
Also, to put out there, one thing about the collector side of things.
We, the current iteration is basically just large tables in the documentation. And so if anyone has ideas about how to better present that information than just a table.
We would be very grateful for your input. You can… I'm sure Jay will put a link to the docs in there where I can add it.
so you can see what it looks like right now. But, yeah, we're… it's… it's something that's not super high priority, but I'm… I'm hopeful that someone out there in the community has ideas and… and can bring them here.
**Jay DeLuca** 34:35 Yeah, we can certainly… like, the way that I look at those pages, but even the Ecosystem Explorer itself is, like, I'm not a designer, and, like, I can come up with something and get us the starting space, but yeah, if we have… if there's anybody here, or if anyone here knows other people who have an eye for this kind of thing.
definitely send them our way. Even if they can only do it on, like, a consulting basis, like, even if we can just pick their brain and they can give us some high-level you know, ideas, that would be… that would be really great.
**Leandro Caracciolo** 35:08 I can take a look on the, on the contents, I can, so that's something…
**Jay DeLuca** 35:14 Sweet.
**Leandro Caracciolo** 35:14 Here's the.
**Jay DeLuca** 35:17 Yeah, are you a designer?
Andrew.
Awesome.
**Leandro Caracciolo** 35:21 Yep.
**Jay DeLuca** 35:22 Cool. Yeah, so this is the… this is the page that, we were just talking about. So we just added these pages in, so it's very basic. We just have these tables with these… we have receivers, processors, exporters, I think extensions is probably the most complex in the sense that it just has multiple tables, but yeah, essentially, we've started with a very small amount of information, and we eventually want to display More, and we just… I'm a little scared, because it already doesn't look too great, I already lost the page, but yeah. Anyway, yeah, if you have ideas, that would be… that would be awesome. You can either… we have a, a Slack channel, You can just come and chat in that, or you can bring it up in these messages, or ping one of us directly, but yeah, if you have any thoughts at all, that would be great.
**Leandro Caracciolo** 36:17 I can just…
**Severin Neumann** 36:17 I mean, Jay Leandro, also don't hesitate to meet one-off if you feel like, hey, we want to play back some ideas on that. I think, like… I think this is also, like, for the visualization part, like.
before you even said, like, hey, I can help you with that, I was like, hey, maybe Leandro can help you with that. So I'm excited that you signed up for that.
**Tiffany Hrabusa** 36:39 That's why I mentioned it. I was kind of hoping Leandro was.
**Severin Neumann** 36:42 pick up.
**Leandro Caracciolo** 36:43 Every time, every time I hear the word designer, I don't talk, maybe, maybe I can help with that, no?
**Severin Neumann** 36:48 Yeah, it would be pretty cool, yeah, yeah.
Yeah, cool.
Yeah, as you said, December is really slow, and what is not slow about is December is everybody's, like, wrapping up a lot of stuff. At least I feel like I have more work to do than days left.
But yeah, I think that we hopefully can hit some speed in early next year, and get maybe also more people excited about this project.
I don't know, anything… anything else we'd like to… to chat about that, or do we want to… Get a few other things talked about.
**Marylia Gutierrez** 37:26 I was gonna say, just a reminder about people disappearing. The last two weeks of December, all sick meetings are canceled, so not just for this sick, but everybody, like, all the others, so people will definitely disappear.
**Severin Neumann** 37:42 Yeah, exactly. So we won't have a meeting, that's a good call-out on… on the 23rd, obviously, and I think then we're back… I think at the 6th.
Yeah.
No.
No? Yeah, yeah, we are. December's… January 6th, so… so we're back then.
I might not be able to make it down because I'm traveling, but yeah, we will figure out.
Awesome. Maybe we can put this… I don't know who's having the thing open, that we maybe add a note on that, that, like, there will be no meeting.
Next time, we can… can add that.
Yeah, exactly. I think we have one more item on the agenda, or is there anything else we'd like to chat about? If not, like, I can… I can quickly throw that out. Vitor, I just added you to that because you brought it up.
So we had a little bit the idea to standardize a little bit more on good GitHub actions. One of them is this action on creating pull requests, but on the other hand, like, right now, there's this whole How is this, like, like, this, supply chain attack?
underway with, like, especially in the JavaScript universe.
So I think that the big question is, like, what are we going to do with that in the future? I mean, there's a lot of… moving parts on that. I think one piece is that, like, we already have a bunch of active GitHub Actions.
And one thing, like, we rolled out across, the whole OpenTelemetry GitHub org is the OpenSSF scorecard.
Which tries to… Call out any kind of, flaws, or, like, or no, it tries to establish best practices, and for example, one of them is, like, for GitHub Actions to pin… the versions, but I'm not exactly sure if this is helping in that specific situation, and like, if we pin the GitHub runners and the actions, if this is going to help, or if we need to do the same thing for… for our package JSON.
I think there, right now, we are not pinning the specific versions. I don't know if anybody here has good ideas or thoughts on that topic, or can help with that, so it's just a thing I wanted to call out.
**Jay DeLuca** 40:41 The, this particular one, I think I helped with a couple… migrations in the Java repo, like, I… at least for, like, the GitHub, like, PR creation, or… or whatever, like, I think there's ways to do it.
pretty easily without relying on the GitHub action, so… From my sta… from my opinion, it makes sense to invest in Removing those, because… That is kind of a… A higher risk entry point.
But in terms of overall, I don't… I don't have any… strong opinions, but I do think that, at least for something like this, I think they're… It's not a huge lift to… Just remove the risk.
**Severin Neumann** 41:26 What was Java doing? Like, did Java remove more GitHub actions, or did they, like, pick the good ones, so to speak?
**Jay DeLuca** 41:35 I think we were… we removed all the ones that created PRs, at least.
I could probably find… an example.
But I think I did one that removed this particular.
**Severin Neumann** 41:50 Yeah, action by Peter Evans, I think his name is. So, okay, yeah, he removed that. I think the thing I liked about it is, like, it also manages, like, existing PRs and can, like, add commits and something like that. We partially use that.
But if you… if you have a better solution for that, or something that can, like, do this without Like, yeah, less dependencies is definitely, like… It seems like the… The trend of the day, because of all those attacks.
But if you can comment on that pull request with whatever you have.
It would be helpful, yeah.
**Jay DeLuca** 42:28 Yeah, actually, it looks like it was a different one.
But I'll put it here anyway.
**Severin Neumann** 42:32 Yeah, that would be cool.
Yeah, beyond that, I think that's just something we need to spend more time on.
The next few weeks and months to… to establish A little bit better.
protection for some of these things we're running. But if nobody else has any comments, I just wanted to bring it up here.
Anything else?
I mean, I have a few topics in my mind, but I thought, like, yeah, let's look at them next year, or offline. So yeah, if there's nothing else, and since we won't meet in two weeks from now, I… I wish you all a good… break.
Oh yeah, Leandro, please.
**Leandro Caracciolo** 43:32 Oh, sorry, just one quick update about those social media assets that I did.
I… I did some tests on PainPot, so I get some layout from Figma to PaintPot, and it gave me good results, so I just have to read up the text on it, so… but it works, so I think it's a good possibility, if you want to, to keep Google… to keep assets on Google Slides for known designers, and import for designers, if you think it's a good idea, so just…
**Severin Neumann** 44:02 Okay, that's good to hear, yeah. I mean, I mean, we still have time, so if you want to share something right now, but otherwise, I mean, if you like, say, like, hey, I can do a quick intro or a write-up early next year, that's how you like, right? I mean…
**Leandro Caracciolo** 44:21 Okay.
**Severin Neumann** 44:30 So do you prefer, like, do you want to show us something right now, or should we do this next time? No, I will do this. I will do the other ones, and I'll show everything to you. Okay. Perfect, perfect, and then let's do this next year, and thank you for doing that, that's really, that's really great.
**Leandro Caracciolo** 44:46 You're welcome.
**Severin Neumann** 44:47 Awesome. Cool.
Dan, yeah, once again, have a… for those of you who take a break, I was going to take a break, and enjoy that break, and independent of Dan, yeah, Happy New Year already, and then, yeah, talk to you on Slack, and then see you in 2026.
**Jay DeLuca** 45:08 Good seal.
**Vitor Vasconcellos** 45:08 Happy Holidays!
**Jay DeLuca** 45:10 You too. Bye.
**Leandro Caracciolo** 45:11 Happy Holidays!
**Vitor Vasconcellos** 45:12 Teo. Alright, headphones.
