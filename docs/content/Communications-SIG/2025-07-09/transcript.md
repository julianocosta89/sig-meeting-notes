SIG: Communications SIG
Date: 2025-07-09
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**TH Tiffany Hrabusa** 01:27 Hi lisa! Hi! Sophia!
**Lisa Jung** 01:36 Hello!
**TH Tiffany Hrabusa** 01:39 We'll give it another minute or 2 and see if anyone else is joining. I haven't heard from any of the other Maintainers to know if they're coming or not. So.
**Lisa Jung** 01:49 That's good.
**TH Tiffany Hrabusa** 01:52 And if you have anything that you would like to talk about, you can add it to the agenda, or you can tell me, and I can add it to the agenda. Do you, Sophia? Do you have the link to the the notes document?
**Sophia Solomon** 02:03 I don't. Can you send it in the chat?
**TH Tiffany Hrabusa** 02:07 Yep.
**Sophia Solomon** 02:08 Cool.
**TH Tiffany Hrabusa** 02:11 There you go!
**Sophia Solomon** 02:13 Cool.
**TH Tiffany Hrabusa** 02:28 I do know that Fabrizio is on vacation.
and I think and so is Patrice.
And I think, Severn said that he was at an offsite this week, so I think maybe he will not be joining but I haven't heard from Philip.
So yeah, I don't have anything other than a quick update on the collector docs refactoring.
So if either of you have something that you want to talk about first, st we can do that or.
**Lisa Jung** 03:06 No, not this week.
**Sophia Solomon** 03:07 Yeah, I don't have anything. I'm still finding, trying to find ways to like contribute. So I mean, if you have.
**TH Tiffany Hrabusa** 03:14 Absolutely.
**Sophia Solomon** 03:16 Yeah.
**TH Tiffany Hrabusa** 03:18 Yeah.
this is a good place to start. I think summer is a little slow. Things tend to slow down a bit. So.
But yeah, usually we have an a full agenda for these meetings. So.
**Sophia Solomon** 03:33 Cool.
**TH Tiffany Hrabusa** 03:35 on the collector docs refactoring. I spent last week coming up with game plan right now. It's in my personal task tracker like I haven't created a public facing document yet, but I think the 1st thing I'm going to do is analyze all of the slack data that I have, which is like over 4 years worth And I'm basically going to pull out like, what are the top complaints about documentation, which are the top pages that get consulted like if people are saying I checked this page and they're not necessarily talking about whether the docs lacked something or not. But it's a page that they're consulting. Then that means we need to pay more attention to it, right? That it's it's something that people are using as a reference. And then I also just wanna see what?
What types of topics like.
not even thinking about docs in in the content of the slack messages. But just what kinds of topics are people in the community coming to slack to find answers to like? They may not even mention the docs. But if there's a repeated, if there's a theme for things that people are coming to because they can't find the answers somewhere else, they may not even be thinking about checking the documentation, but I think that that's somewhere that we should probably try to help them a little bit more. So that's something I'm gonna work on this week. I'm also waiting for Patrice to come back so that he can help me.
Pull some of the analytics that we have for the website. So we have some very basic, I can show you in case you were not aware.
Okay, so can you see my screen.
**Sophia Solomon** 05:43 Sure.
**TH Tiffany Hrabusa** 05:44 Okay.
So if you go to the bottom of any website or any page on the opentelemetryio website, there's a button down here for site analytics.
And so anybody can go and check this out.
But it's very anonymized, and it's not very granular. And I'm pretty sure that the maintainers like the actual site maintainers have more detail that I can draw from. So I'm just gonna see. But you can see like.
I don't know what the time. Okay, so this is the last month.
And the collector homepage is the second most consulted page in the docs, whereas the actual landing page.
The open telemetry homepage is the top spot.
And then there's a couple other collector pages that factor into the top 10. So that was one of our justifications for doing this project is that people are using these docs, but they're not getting what they need out of them. So I just want to use this this type of data to pinpoint exactly where we should target our efforts, because obviously, we all have limited time and we would like to make some progress ideally before kukan, North America.
so yeah, that's that's kind of the the framing that we're going with.
And I say we. But right now it's really just yeah.
Yeah. So let me stop sharing.
I have a couple contacts in the collector, Sig, and they are Ostensibly they are on board. They want this to happen, but they are also stretched incredibly thin. So I'm trying not to impose on them. Which is why I'm trying to pull insights from this wealth of information that we already have. Right like it's there. I just need to figure out how to access it and organize it. And so, yeah, that's kind of where I'm starting. And then I think my plan is to kind of create a more focused I guess work plan, create issues related to each specific task. So that there's like, we can actually measure progress that we're getting things done. And once I get to that point, once I have something that I can actually show people and say, this is this is where we're gonna go with this. And this is what we need help on.
Then I will think about how to organize a team effort on this, because I think too many cooks in the kitchen early on means that you just kind of have this like inertia, where nobody's making decisions right? Like nobody's saying, okay, this is where we need to go. So.
**Sophia Solomon** 08:51 Right.
**TH Tiffany Hrabusa** 08:52 Yeah. So I'm gonna do the the kind of background research 1st and figure out which areas we need to target specifically, there's also part of this project is going to be just reorganizing or refactoring the in information architecture of the documentation which I don't want to do on my own, because I am not a user. So there may be some like A B testing. I might do with, you know, if I can find some users who are willing to talk to me like what makes more sense from their perspective when they go looking for something. And I actually tried to add a bunch of questions to the I think that is it. The end user? Sig, I think, is doing a survey for the collector itself.
**Sophia Solomon** 09:40 Oh!
**TH Tiffany Hrabusa** 09:41 And I tried to wheedle my way in there and say, Hey, can you ask some docs questions? But it's already a pretty lengthy survey. So they they agreed to ask one question about docs. I mean, there's like the initial question, do you use the docs? And then like, what's your opinion of the docs? But then I had a couple of like free text boxes like, I wanted to ask.
Have you gone to the documentation looking for something and not been able to find it like.
And if so, what was it like?
And then, you know, just things like that, like specific specific questions, but they would have a free text box that people could kind of talk about. But the one question I got in was, if you could change one thing about the documentation. What would it be?
So we'll see hopefully, I'll get some information there. But yeah, I think I think I don't. Wanna I don't wanna do another survey on top of that one because people aren't gonna respond. So what I might do is just ask in the hotel collector slack channel. And just say.
would anyone be willing to talk to me and just like do a much smaller sample size, but more but more in depth, interviewing of of like users. So anyway, those are my ideas. If you have thoughts about resources I should tap into, or as far as like doing all of this background research. I'm absolutely willing to take all of your input there. So.
**Lisa Jung** 11:21 Yeah. So while I was going through like the hotel collector docs, I wish they had, like a list of processors and brief descriptions. The only place I could find that was like a separate Github page. But I've not actually within the docs. So that that's something that I wanna add.
**TH Tiffany Hrabusa** 11:37 Yep.
**Lisa Jung** 11:38 Yeah.
**TH Tiffany Hrabusa** 11:38 That is a it's a i'm gonna make a note that you said that. But It's a huge huge topic that comes up every time we talk about the collector documentation is why why is the component documentation? Not in opentelemetry, dot I/O. And there is actually a really good reason for that it has. They've talked about it. And every time they come to the same decision, which is that the component documentation changes pretty frequently, and it's each component is handled by a different set of code owners. Right? Like there, there are a very small, like a handful of components that are part of the core collector distribution.
**Lisa Jung** 12:24 Commute.
**TH Tiffany Hrabusa** 12:25 But the rest of them are in contrib, and they're built, you know, like.
vendors create components like there's all different kinds of things.
The idea is, if you keep the documentation close to the code that is being changed, that the documentation stays up to date, and it also means that the the code developers are more likely to update that documentation.
**Lisa Jung** 12:48 I see.
**TH Tiffany Hrabusa** 12:50 and they're the like. The project leaders, collector and otherwise, are hesitant to move that out like they really don't want to move the documentation out of the Repository.
**Lisa Jung** 13:05 Gotcha. Yeah, I didn't have that back.
**TH Tiffany Hrabusa** 13:07 There are. There are ways. Yeah. You didn't realize you were opening a can of worms right? But but no, it's it's actually one of the top things that we are going to try and address this in this next refactoring. I think I think it will be an iterative process.
There's there's a few things we can do at the very minimum. We can create a list like you, said with a brief description. There's also the registry, which is part of the website. But it's separate. Like, it's not How do I?
It's not. It's it has like different functionality. It's not just like a HTML page that's built by Hugo. So there might be ways that we can pull in more of the documentation into the registry like more of the metadata surrounding the components, so that the registry entries are more complete.
And then, somehow high like that list in the documentation to the registry which then links to the you know there are, there are definitely incremental steps we can make to improve the experience for users as far as the component documentation. But the way I understand it right now, one of those steps will not be relocating that documentation out of the collector contribute repository and into the website repository.
But yeah, thank you.
**Lisa Jung** 14:43 There is.
Yes, if there is a way to even like Hyperlink, that page, that repo within the Doc would be helpful, because I was like looking all over like the collector docs and like, Where where is this? And then I Google searched it. And then I found the repo. So if you could just add the hyperlink somewhere like very visible, I mean, that'd be like the low hanging fruit.
**TH Tiffany Hrabusa** 15:08 Yep, I think I think there is a section that has a a small link.
It says, like, if you're looking looking for other components go here, but it's like a sentence buried in a.
**Lisa Jung** 15:24 Yeah.
**TH Tiffany Hrabusa** 15:25 Long page, and it's definitely not called out. So yes, we will definitely improve the component documentation to the.
**Lisa Jung** 15:49 Or is it I? I don't know how this works, but like, is it possible to have a category on the on, like the menu website or the website menu, and then hyperlink it. There is that possible.
**TH Tiffany Hrabusa** 16:06 Oh,
**Sophia Solomon** 16:10 Hmm.
**TH Tiffany Hrabusa** 16:11 I don't know. I mean, I think I mean, I think you can turn any link into an external link.
You just have to point it. The question is whether.
from a like website design perspective, do you want something in your native menu to take you outside of the website? But I think that's the only way we could just create a blind landing page like we could have like a component documentation. And then it's just a landing page that says, Go here. Or, Yeah, that would be, I think, okay. But I think, like, directly linking from the menu might be, not a website designer. So I don't know. Adding hyperlinks to the website findable, maybe from the navigation menu.
Where are you? Landing age?
Also, let me.
Yeah.
It's I mean, it's the the age old problem of documentation keeping it up to date. Right? So I think the Collector Maintainers have been very firm about the fact that they want the component documentation to be accurate and up to date, and they've put their foot down like it stays where it is, because that's the only way that's going to happen like, if the if the documentation is moved elsewhere, developers are going to just change their component, and the documentation is never going to get updated.
So yeah, it's tricky. And the other.
the other problem is that there's new components getting, added.
I mean, maybe not quite as frequently as they used to, but they are getting added. And so it's like.
that's where you get like. Even creating a list could quickly become out of date if.
**Lisa Jung** 18:20 But yeah.
I mean for me, it's like, as long as I could like find it within the document, I mean, not within the documentation, but like, Oh, here's where to go, if you need it. Yeah, that'd be.
**TH Tiffany Hrabusa** 18:30 Yeah, okay.
**Lisa Jung** 18:31 Helpful. Yeah.
**TH Tiffany Hrabusa** 18:32 Findability was key.
Okay. Sophia, do you have any thoughts on anything? All of the all of the very wordy explanations I've been giving.
**Sophia Solomon** 18:46 Yeah, no. I mean, I like the idea of a landing page, especially if it's hard to find.
I mean, my initial thought is like to build something that will like.
Take all those descriptions that the individual developers use on the collectors, and then, like aggregates them as they come along, but I think that's maybe more complicated than what your project is looking for.
**TH Tiffany Hrabusa** 19:13 Well, so that's funny. You should say that that is kind of what the registry already does like.
there's a little bit of automation. Let me let me find, and I'll show you what the registry looks like.
Okay, share again.
Oh, okay, so this is just you can get here from the ecosystem page on the website. And it's basically all of the all of the components.
Of open telemetry. So you've got sdks you've got like any kind of instrumentation tools. You've got the collector components, every part of open telemetry, and this includes 3rd party stuff as well like. It's not just native hotel things. So anybody who has created any kind of component that works with open telemetry can create an entry in the registry. So like if we search for like debug. So we've got the debug exporter. And then there's an extension here. So this is where they would like to pull in. So it does link. You see it does link oh, to directly to the repository where that documentation is found.
but it doesn't pull all of the metadata in directly to the registry itself. So the idea is, instead of sending people out. Maybe we can improve the integration that exists. And pull more of the metadata. So let me see, I think I had Where did I put it?
of course I can't find it now. I took notes. Oh, you know what I link. I sent them in slack. Let's see if I can find it. One second.
**Sophia Solomon** 21:48 Hmm.
**TH Tiffany Hrabusa** 21:58 Sorry one second. I know I have it here somewhere, but
**Sophia Solomon** 22:02 No rush.
**TH Tiffany Hrabusa** 22:04 There's a specific list of metadata that they are hoping to include.
**Sophia Solomon** 22:13 Okay.
**TH Tiffany Hrabusa** 22:18 Just need to find it.
Know what I did with it?
I will find it at some point when I don't need it anymore. But
**Sophia Solomon** 22:43 We are staring at you right.
**TH Tiffany Hrabusa** 22:47 There's a list of metadata that the collector folks would like to have in the registry that they think would be beneficial.
not the complete documentation, but it would improve the experience. So yeah, that's definitely one of the top. I would say, top 3 things that I plan to work on. So one is just information architecture refactoring.
2 is at this point mostly just identifying gaps like, I would say, the the component documentation qualifies as a gap, but it's kind of in its own category. The rest would be things that should be covered in the documentation, in the existing documentation. And just either isn't like it's non existent.
or it's not covered completely enough like the what's there doesn't get you all the way to where you need to be.
**Sophia Solomon** 23:45 Right.
**TH Tiffany Hrabusa** 23:46 I don't know how far we'll be able to make like filling those gaps, but I think just identifying them and creating some concrete plans for okay, we need to. We need to liaise with a collector person who knows how to explain. Xyz.
And then, you know, we can, Async like, get with them and say, How can we improve this documentation?
Use cases is another thing people want. But that's like again, age, old documentation, like everybody, wants more examples and use cases. So that is a category of the gaps that I would like to identify like. And I think that's where, like the slack information is going to help inform, like.
what are these use cases that people are trying to do? And our documentation doesn't guide them through that. So.
**Sophia Solomon** 24:42 Right.
**TH Tiffany Hrabusa** 24:43 And then the 3rd category is just starting to improve the user experience for component documentation. And I think, like I said, it'll be a slow process to get it to where I think we want it to be. But in the meantime it'll probably be like stopgap kind of things like creating a list or creating a landing page that links to the repository.
or maybe creating a static list that you know, we would have to keep updated at this point in time.
Yeah, so that's I'll add more notes to this document. So people don't. Just.
I think that I just said collector dogs refactoring. And that's it.
And you know, going into August when everybody disappears, it means that we're probably gonna not be making much headway on this until September.
But I that's why I'm kind of thinking if I do the background work on my own without having to tax anyone else's time. In the next, like 6 weeks or so. 8 weeks.
6, 7 weeks.
We'll be well positioned to kind of get started in September, when people are back.
**Sophia Solomon** 26:08 Awesome.
**TH Tiffany Hrabusa** 26:09 Okay. I talked for like a half an hour. Does anyone have anything else they want to talk about?
Okay. Alright. Then I'll I don't know about that, but you know this meeting is recorded for posterity, so it's not like I can ever say that I don't speak up in meetings right? Or that I'm not.
I'm I'm very shy, and I don't talk. I don't know what you're talking about. There's no video evidence to the contrary. But yeah. So, Sophia, I'm glad you're here. I'm sorry we don't have much in the, you know, as far as like what there is to do. I do think that will change once people are back from their travels and stuff. So please keep joining us.
**Sophia Solomon** 26:58 Well.
**TH Tiffany Hrabusa** 27:00 If nothing else, you'll be entertained by my my, stand up routine here. But if you have anything.
you know any questions, or if you need any support in between meetings, you can also reach us on slack. You know that? Right? Yeah.
Okay, yeah. Because most of us are there most of the time. So, okay.
**Sophia Solomon** 27:24 Sure.
**TH Tiffany Hrabusa** 27:25 Have a great day.
**Sophia Solomon** 27:28 Bye, bye.
**TH Tiffany Hrabusa** 27:30 Okay.
